import caffe

solver=caffe.SGDSolver("/home/deepl/Documents/wb/my_tf_caffe/my_caffe/net/lenet_solver.prototxt")

solver.solve()
