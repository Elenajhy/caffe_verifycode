# caffe_verifycode
 # -Automatic-recognition-of-verification-code-based-on-deep-learning-method
Automatic recognition of verification code based on deep learning method <br>
data:	 <br>
1.train_nosplit:未分割的训练集验证码图片，共1000张 <br>
test_nosplit:未分割的测试集验证码图片，100张 <br>
2.运行split_verifycode.py: <br>
train_nosplit分割后为4000张（每张验证码4个字符），保存在data/train_split文件夹中 <br>
test_nosplit分割后为400张（每张验证码4个字符），保存在data/test_split文件夹中 <br>
caffe_verifycode: <br>
3.编写test.txt与train.txt标签文件，label是直接拿的别人用的，后面测试模型要用到。 <br>
4.根据txt文件与分割后的数据集转换成lmdb格式保存在data/test or train_lmdb目录下 <br>
5.根据txt文件与分割后的数据集生成均值文件mean.binaryproto。 <br>
6.模型训练和测试 <br>
