import tensorflow as tf
import numpy as np
# import os, sys, inspect
from datetime import datetime
import EmotionDetectorUtils
 
 
FLAGS = tf.flags.FLAGS
tf.flags.DEFINE_string("data_dir", "EmotionDetector/", "Path to data files")
tf.flags.DEFINE_string("logs_dir", "logs/EmotionDetector_logs/", "Path to where log files are to be saved")
tf.flags.DEFINE_string("mode", "train", "mode: train (Default)/ test")
 
BATCH_SIZE = 128
LEARNING_RATE = 0.001  # 学习率
MAX_ITERATIONS = 1001  # 最大迭代次数
REGULARIZATION = 1e-2  # 正则项参数大小
IMAGE_SIZE = 48  # 图像大小
NUM_LABELS = 7  # 输出的类别数量
VALIDATION_PERCENT = 0.1
 
# 添加正则项
def add_to_regularization_loss(W, b):
    tf.add_to_collection("losses", tf.nn.l2_loss(W))
    tf.add_to_collection("losses", tf.nn.l2_loss(b))
 
# 按照传递进来的shape形状初始化权重
def weight_variable(shape, stddev=0.02, name=None):
    initial = tf.truncated_normal(shape, stddev=stddev)
    if name is None:
        return tf.Variable(initial)
    else:
        return tf.get_variable(name, initializer=initial)
 
# 初始化偏差
def bias_variable(shape, name=None):
    initial = tf.constant(0.0, shape=shape)
    if name is None:
        return tf.Variable(initial)
    else:
        return tf.get_variable(name, initializer=initial)
 
 
def conv2d_basic(x, W, bias):
    conv = tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")
    return tf.nn.bias_add(conv, bias)
 
# 池化层操作
def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding="SAME")
 
# 模型的实现
def emotion_cnn(dataset):
    print("input dataset's shape-->", dataset.shape)
    with tf.name_scope("conv1") as scope:
        tf.summary.histogram("W_conv1", weights['wc1'])
        tf.summary.histogram("b_conv1", biases['bc1'])
        conv_1 = tf.nn.conv2d(dataset, weights['wc1'],
                              strides=[1, 1, 1, 1], padding="SAME")
        print("conv_1's shape--->", conv_1.shape)
        h_conv1 = tf.nn.bias_add(conv_1, biases['bc1'])
        h_1 = tf.nn.relu(h_conv1)
        # h_pool1 = max_pool_2x2(h_1)
        # print("h_pool1 shape-->", h_pool1.shape)
        add_to_regularization_loss(weights['wc1'], biases['bc1'])
 
    with tf.name_scope("conv2") as scope:
        tf.summary.histogram("W_conv2", weights['wc2'])
        tf.summary.histogram("b_conv2", biases['bc2'])
        # conv_2 = tf.nn.conv2d(h_pool1, weights['wc2'], strides=[1, 1, 1, 1], padding="SAME")
        conv_2 = tf.nn.conv2d(h_1, weights['wc2'], strides=[1, 1, 1, 1], padding="SAME")
        print("conv_2's shape--->", conv_2.shape)
        h_conv2 = tf.nn.bias_add(conv_2, biases['bc2'])
        h_2 = tf.nn.relu(h_conv2)
        h_pool2 = max_pool_2x2(h_2)
        add_to_regularization_loss(weights['wc2'], biases['bc2'])
 
    with tf.name_scope("conv3") as scope:
        tf.summary.histogram("W_conv3", weights['wc3'])
        tf.summary.histogram("b_conv3", biases['bc3'])
        conv_3 = tf.nn.conv2d(h_pool2, weights['wc3'], strides=[1, 1, 1, 1], padding="SAME")
        print("conv_3 shape-->", conv_3.shape)
        h_conv3 = tf.nn.bias_add(conv_3, biases['bc3'])
        h_3 = tf.nn.relu(h_conv3)
        # h_pool3 = max_pool_2x2(h_3)
        # print("h_pool3 shape-->", h_pool3.shape)
        add_to_regularization_loss(weights['wc3'], biases['bc3'])
 
    with tf.name_scope("conv4") as scope:
        tf.summary.histogram("W_conv4", weights['wc4'])
        tf.summary.histogram("b_conv4", biases['bc4'])
        # conv_4 = tf.nn.conv2d(h_pool3, weights['wc4'], strides=[1, 1, 1, 1], padding="SAME")
        conv_4 = tf.nn.conv2d(h_3, weights['wc4'], strides=[1, 1, 1, 1], padding="SAME")
        print("conv_4 shape-->", conv_4.shape)
        h_conv4 = tf.nn.bias_add(conv_4, biases['bc4'])
        h_4 = tf.nn.relu(h_conv4)
        h_pool4 = max_pool_2x2(h_4)
        print("h_pool4 shape-->", h_pool4.shape)
        add_to_regularization_loss(weights['wc4'], biases['bc4'])
 
    with tf.name_scope("fc_1") as scope:
        prob = 0.5
        image_size = IMAGE_SIZE // 4
        h_flat = tf.reshape(h_pool4, [-1, image_size * image_size * 128])
        print("h_flat shape--->", h_flat.shape)
        tf.summary.histogram("W_fc1", weights['wf1'])
        tf.summary.histogram("b_fc1", biases['bf1'])
        h_fc1 = tf.nn.relu(tf.matmul(h_flat, weights['wf1']) + biases['bf1'])
        print("h_fc1'shape--->", h_fc1.shape)
        h_fc1_dropout = tf.nn.dropout(h_fc1, prob)
        print("h_fc1_dropout shape-->", h_fc1_dropout.shape)
 
    with tf.name_scope("fc_2") as scope:
        tf.summary.histogram("W_fc2", weights['wf2'])
        tf.summary.histogram("b_fc2", biases['bf2'])
        pred = tf.matmul(h_fc1_dropout, weights['wf2']) + biases['bf2']
        print("pred shape-->", pred.shape)
 
    return pred
 
 
weights = {
    'wc1': weight_variable([3, 3, 1, 64], name="W_conv1"),
    'wc2': weight_variable([3, 3, 64, 64], name="W_conv2"),
    'wc3': weight_variable([3, 3, 64, 128], name="W_conv3"),
    'wc4': weight_variable([3, 3, 128, 128], name="W_conv4"),
    'wf1': weight_variable([(IMAGE_SIZE // 4) * (IMAGE_SIZE // 4) * 128, 256], name="W_fc1"),
    'wf2': weight_variable([256, NUM_LABELS], name="W_fc2")
}
 
biases = {
    'bc1': bias_variable([64], name="b_conv1"),
    'bc2': bias_variable([64], name="b_conv2"),
    'bc3': bias_variable([128], name="b_conv3"),
    'bc4': bias_variable([128], name="b_conv4"),
    'bf1': bias_variable([256], name="b_fc1"),
    'bf2': bias_variable([NUM_LABELS], name="b_fc2")
}
 
 
def loss(pred, label):
    cross_entropy_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=pred, labels=label))
    tf.summary.scalar('Entropy', cross_entropy_loss)
    reg_losses = tf.add_n(tf.get_collection("losses"))
    # tf.summary.scalar('Reg_loss', reg_losses)
    return cross_entropy_loss + REGULARIZATION * reg_losses
 
 
def train(loss, step):
    return tf.train.AdamOptimizer().minimize(loss, global_step=step)
 
 
def get_next_batch(images, labels, step):
    offset = (step * BATCH_SIZE) % (images.shape[0] - BATCH_SIZE)
    batch_images = images[offset: offset + BATCH_SIZE]
    batch_labels = labels[offset:offset + BATCH_SIZE]
    return batch_images, batch_labels
 
 
# 入口函数
def main(argv=None):
    # 获得数据
    train_images, train_labels, valid_images, valid_labels, test_images = EmotionDetectorUtils.read_data(FLAGS.data_dir)
    print("Train size: %s" % train_images.shape[0])
    print('Validation size: %s' % valid_images.shape[0])
    print("Test size: %s" % test_images.shape[0])
 
    # 定义global_step变量追踪当前已进行优化迭代次数,trainable=Flase意为Tensorflow不会试图优化该变量
    global_step = tf.Variable(0, trainable=False)
    dropout_prob = tf.placeholder(tf.float32)
    # 为输入图像定义占位符变量 None表示该张量可以载入任意数量的图像，每个图像高和宽都为IMAGE_SIZE像素，颜色通达数为1
    input_dataset = tf.placeholder(tf.float32, [None, IMAGE_SIZE, IMAGE_SIZE, 1], name="input")
    # 为输入input_data中的图像真实标签定义占位符变量
    input_labels = tf.placeholder(tf.float32, [None, NUM_LABELS])
    # 获得网络输出
    pred = emotion_cnn(input_dataset)
    # output_pred变量为预测结果，用于网络的测试和验证
    output_pred = tf.nn.softmax(pred, name="output")
    correct_prediction = tf.equal(tf.argmax(output_pred, 1), tf.argmax(input_labels, 1))
    # tf.cast(x, dtype, name=None) 将输入转换成dtype的类型
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    tf.summary.scalar("accuracy", accuracy)
    # loss_val变量为预测的类（pred）和输入图像的真实类（input_labels)之间的的误差
    loss_val = loss(pred, input_labels)
    # 获得优化器对象实例
    train_op = train(loss_val, global_step)
    # 定义summary_op变量用于Tensorboard可视化
    summary_op = tf.summary.merge_all()
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        summary_writer = tf.summary.FileWriter(FLAGS.logs_dir, sess.graph_def)
        # 定义saver变量，以存储该模型
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(FLAGS.logs_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            print("Model Restored!")
        # 开始训练
        for step in range(MAX_ITERATIONS):
            # 获得batch_size大小的一批训练样本
            batch_image, batch_label = get_next_batch(train_images, train_labels, step)
            # print("batch image's shape--->", batch_image.shape)
            feed_dict = {input_dataset: batch_image, input_labels: batch_label}
            # 运行优化器，将对应占位符的数据传递进去
            sess.run(train_op, feed_dict=feed_dict)
            if step % 10 == 0:
                train_loss, summary_str = sess.run([loss_val, summary_op], feed_dict=feed_dict)
                summary_writer.add_summary(summary_str, global_step=step)
                print("Training Loss: %f" % train_loss)
            # 当运行步数为100的倍数时，在验证集上验证训练出的模型，并且保存该模型
            if step % 100 == 0:
                valid_loss = sess.run(loss_val, feed_dict={input_dataset: valid_images, input_labels: valid_labels})
                print("%s Validation Loss: %f" % (datetime.now(), valid_loss))
                print("Accuracy: ", accuracy.eval(feed_dict={input_dataset: valid_images, input_labels: valid_labels}))
                saver.save(sess, FLAGS.logs_dir + 'model.ckpt', global_step=step)
 
 
if __name__ == "__main__":
    tf.app.run()