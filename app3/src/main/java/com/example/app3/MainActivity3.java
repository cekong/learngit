package com.example.app3;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.srplab.www.starcore.*;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

public class MainActivity3 extends Activity {

//    static {
//        System.loadLibrary("native-lib");
//    }


    public StarSrvGroupClass SrvGroup;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);

        TextView tv1 = (TextView) findViewById(R.id.sample_text1);
        TextView tv2 = (TextView) findViewById(R.id.sample_text2);
        TextView tv3 = (TextView) findViewById(R.id.sample_text3);
        TextView tv4 = (TextView) findViewById(R.id.sample_text4);
        TextView tv5 = (TextView) findViewById(R.id.sample_text5);

        File destDir = new File("/data/data/" + getPackageName() + "/files");
        if (!destDir.exists())
            destDir.mkdirs();
        java.io.File python_libFile = new java.io.File("/data/data/" + getPackageName() + "/files/python3.6.zip");
        if (!python_libFile.exists()) {
            try {
                copyFile(this, "python3.6.zip", null);
            } catch (Exception e) {
                System.out.println("zipzipzipzip///  " + e);
            }
        }
        try {
            copyFile(this, "add.py", "");
        } catch (Exception e) {
            System.out.println("addaddaddadd///  " + e);
        }
        try {
            copyFile(this, "_datetime.cpython-36m.so", null);
            copyFile(this, "zlib.cpython-36m.so", null);
        } catch (Exception e) {
            System.out.println("zlibzlibzlibzlib/// " + e);
        }
        try {
            System.load(this.getApplicationInfo().nativeLibraryDir + "/libpython3.6m.so");
            Log.e("aaaaa", "aaaaaaaaaaaaa-->" + this.getApplicationInfo().nativeLibraryDir + "/libpython3.6m.so");
        }catch (UnsatisfiedLinkError ex) {
            Log.e("aaaaa", "bbbbbbbbbbbbbbb");
            System.out.println("bbbbbbbbbb///   " + ex.toString());
            Log.e("ssssss", "qweqweqwe-->" + this.getApplicationInfo().nativeLibraryDir + "/libpython3.6m.so");
        }


        /*----init starcore----*/
        StarCoreFactoryPath.StarCoreCoreLibraryPath = this.getApplicationInfo().nativeLibraryDir;
        StarCoreFactoryPath.StarCoreShareLibraryPath = this.getApplicationInfo().nativeLibraryDir;
        StarCoreFactoryPath.StarCoreOperationPath = "/data/data/" + getPackageName() + "/files";

        StarCoreFactory starcore = StarCoreFactory.GetFactory();
        StarServiceClass Service = starcore._InitSimple("test", "123", 0, 0);
        SrvGroup = (StarSrvGroupClass) Service._Get("_ServiceGroup");
        Service._CheckPassword(false);

        /*----run python code----*/
        SrvGroup._InitRaw("python36", Service); //调用函数_InitRaw初始化python接口
        StarObjectClass python = Service._ImportRawContext("python", "", false, "");
        python._Call("import", "sys");

        StarObjectClass pythonSys = python._GetObject("sys");
        StarObjectClass pythonPath = (StarObjectClass) pythonSys._Get("path");
        pythonPath._Call("insert", 0, "/data/data/" + getPackageName() + "/files/python3.6.zip");
        pythonPath._Call("insert", 0, this.getApplicationInfo().nativeLibraryDir);
        pythonPath._Call("insert", 0, "/data/data/" + getPackageName() + "/files");

        String CorePath = "/data/data/" + getPackageName() + "/files";
        Service._DoFile("python", CorePath + "/add.py", "");
        int _Callint = python._Callint("add_num", 5, 8);
        Log.e("ssssss", "_Callint: " + _Callint);

        Object add_num1 = python._Call("add_num", 1, 6);
        int a = (int) add_num1;
        Log.e("aaa", a + "");

        tv1.setText("python中计算5+8：   " + _Callint + "");
        tv2.setText("python中计算1+6：   " + a + "");
        short[] arrS = {456, 254, 693};  //get_array
        Object get_array = python._Call("get_array", arrS);
        String s = get_array.toString();
//        short[] aaa = (short[]) get_array;
        Log.e("ccc", "aaa.len: " + s);

        Object get_str = python._Call("get_Str");
        Log.e("dddd", "get_str: " + (String) get_str);


        tv3.setText("往python中传递一个数组 {456, 254, 693}，python中获取第一个值并返回：   " + s + "");
        tv4.setText("python返回一个字符串：   " + (String) get_str + "");

        Object get_time = python._Call("get_time");
        Log.e("tttt","get_time: "+get_time);
        tv5.setText("time:"+String.valueOf(get_time)  + "");
    }

    private void copyFile(Activity c, String Name, String desPath) throws IOException {
        File outfile = null;
        if (desPath != null)
            outfile = new File("/data/data/" + getPackageName() + "/files/" + desPath + Name);
        else
            outfile = new File("/data/data/" + getPackageName() + "/files/" + Name);
        outfile.createNewFile();
        FileOutputStream out = new FileOutputStream(outfile);
        byte[] buffer = new byte[1024];
        InputStream in;
        int readLen = 0;
        if (desPath != null)
            in = c.getAssets().open(desPath + Name);
        else
            in = c.getAssets().open(Name);
        while ((readLen = in.read(buffer)) != -1) {
            out.write(buffer, 0, readLen);
        }
        out.flush();
        in.close();
        out.close();
    }
}
