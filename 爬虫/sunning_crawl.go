package main

import (
	"encoding/csv"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"regexp"
	"strconv"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

var gooddetail = []string{"/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"}
var exceltitle = []string{"商品名称", "商品价格", "商品链接", "商品图片", "类别", "口味", "产地", "保质期", "是否含糖", "脂肪含量", "适用人群", "储存方式", "包装", "单件净含量", "包装件数"}

func GetGoodPrice(url string) string {
	re := regexp.MustCompile(`com/(.*?).html`)
	keynum := re.FindAllStringSubmatch(url, -1)
	keynum0 := keynum[0][1]
	key0 := strings.Split(keynum0, "/")[0]
	key1 := strings.Split(keynum0, "/")[1]
	priceurl := "http://pas.suning.com/nspcsale_0_000000000" + key1 + "_000000000" + key1 + "_" + key0 + "_20_021_0210101_500353_1000267_9264_12113_Z001___R9006849_3.3_1___000278188__.html?callback=pcData&_=1558663936729"
	if len(key1) == 11 {
		priceurl = "http://pas.suning.com/nspcsale_0_0000000" + key1 + "_0000000" + key1 + "_" + key0 + "_20_021_0210101_500353_1000267_9264_12113_Z001___R9006849_3.3_1___000278188__.html?callback=pcData&_=1558663936729"
	}

	resp, err := http.Get(priceurl)
	if err != nil {
		panic(err)
	}
	if resp.StatusCode != 200 {
		fmt.Println("err")
	}
	s, _ := ioutil.ReadAll(resp.Body)
	resp.Body.Close()

	re0 := regexp.MustCompile(`"netPrice":"(.*?)","warrantyList`)
	price := re0.FindAllStringSubmatch(string(s), -1)
	fmt.Println(price)
	fmt.Println(priceurl)
	return price[0][1]
}
func GetGoodDetail(url string) {
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	if resp.StatusCode != 200 {
		fmt.Println("err")
	}

	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		panic(err)
	}
	name := doc.Find("div.proinfo-title").Find("h1").Text()
	imageurl, _ := doc.Find("div.imgzoom-thumb-main ul li.current a img").Attr("src-large")
	imageurl = "http:" + imageurl
	price := GetGoodPrice(url)
	doc.Find("tr[parametercode]").Each(func(i int, s *goquery.Selection) {
		gooddetail[0] = name
		gooddetail[1] = price
		gooddetail[2] = url
		gooddetail[3] = imageurl
		key := s.Find("td.name").Text()
		if len(key) > 1 {
			for index, item := range exceltitle {
				if item == strings.Fields(key)[0] {
					value := s.Find("td.val").Text()
					gooddetail[index] = value
				}
			}
		}
	})
}

func GetPagelist(url string, brand string) []string {
	var urls []string
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	if resp.StatusCode != 200 {
		fmt.Println("err")
	}
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		panic(err)
	}
	urls = append(urls, url)
	page, flag := doc.Find("div.search-page").Find("a").Eq(-2).Attr("pagenum")
	pagenum, _ := strconv.Atoi(page)
	if flag {
		for i := 1; i < pagenum; i++ {
			url = "https://list.suning.com/0-500479-" + strconv.Itoa(i) + "-0-0-0-0-0-0-0-" + brand + ".html"
			urls = append(urls, url)
		}
	}
	return urls
}
func GetGoodlist(url string) []string {
	var urls []string

	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	if resp.StatusCode != 200 {
		fmt.Println("err")
	}
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		panic(err)
	}
	doc.Find("div.title-selling-point a").Each(func(i int, s *goquery.Selection) {
		href, _ := s.Attr("href")
		href = "http:" + href
		urls = append(urls, href)
	})
	return urls
}

func main() {
	f, err := os.Create("data.xls")
	if err != nil {
		panic(err)
	}
	defer f.Close()
	f.WriteString("\xEF\xBB\xBF") // 写入UTF-8 BOM

	w := csv.NewWriter(f)
	w.Write(exceltitle)

	var pageurls []string
	var urls []string
	var goodurls []string
	brand := []string{"6063197", "41573", "21530", "4340904"} //伊利、蒙牛、君乐宝、光明
	for i := 0; i < len(brand); i++ {
		url1 := "https://list.suning.com/0-500479-0-0-0-0-0-0-0-0-" + brand[i] + ".html"
		urls = GetPagelist(url1, brand[i])
		pageurls = append(pageurls, urls...)
	}
	// fmt.Println(pageurls)
	for _, url2 := range pageurls {
		urls = GetGoodlist(url2)
		goodurls = append(goodurls, urls...)
	}
	// fmt.Println(goodurls)
	for _, url3 := range goodurls {
		GetGoodDetail(url3)
		// fmt.Println(gooddetail)
		if gooddetail[0] != "/" {
			w.Write(gooddetail)
		}
		gooddetail = []string{"/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/", "/"}
	}
	w.Flush()
}
