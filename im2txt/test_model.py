import tensorflow as tf

from im2txt import configuration
from im2txt.show_and_tell_model import ShowAndTellModel

# filename = "/home/meteorshub/code/im2txt/im2txt/model-backup/inference/test4.jpg"
# ssd300_weights_file = "/home/meteorshub/code/im2txt/im2txt/data/weights_SSD300.hdf5"
# with tf.gfile.GFile(filename, "r") as f:
#     image = f.read()
#
#
# sess = tf.Session()
#
# keras.backend.set_session(sess)
# ssd, good_box = process_image(image, is_training=True, height=299, width=299, ssd300_weights_file=ssd300_weights_file)
# sess.run(tf.global_variables_initializer())
# ssd.load_weights(ssd300_weights_file, by_name=True)
# p = sess.run(good_box)
# # model-backup = SSD300((300, 300, 3))
# # model-backup.load_weights(ssd300_weights_file, by_name=True)
# # model_out = model-backup.predict(np.expand_dims(p, 0))
# # bbox_util = BBoxUtility(21)
# # results = bbox_util.detection_out(np.expand_dims(p, 0))
# i = Image.fromarray((p*255).astype(np.uint8))
# i.save('test.jpg')
#

sess = tf.Session()


model_config = configuration.ModelConfig()
model_config.input_file_pattern = "/home/meteorshub/code/im2txt/im2txt/data/mscoco/train-?????-of-00256"
model_config.inception_checkpoint_file = "/home/meteorshub/code/im2txt/im2txt/data/inception_v3.ckpt"
model_config.ssd300_checkpoint_file = "/home/meteorshub/code/im2txt/im2txt/data/ssd300.ckpt"
with sess:
    model = ShowAndTellModel(model_config, "train")
    model.build()


variables_names = [v.name for v in tf.trainable_variables()]
sess.run(tf.global_variables_initializer())
model.init_fn(sess)

values = sess.run(variables_names)
for k, v in zip(variables_names, values):
    print "Variable: ", k
    print "Shape: ", v.shape