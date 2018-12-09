import tensorflow as tf
import numpy as np


#Setando o seed do tensorflow e numpy com 0 para gerar uma sequencia aleatoria conhecida
tf.set_random_seed(0)
np.random.seed(0)

#número de classes do problema
num_classes = 4
carsList = []

path = 'car.data'
file = open(path,'r')
cars = file.readline()

buyingList = ['vhigh', 'high', 'med', 'low'] 
maintList = ["vhigh", "high", "med", "low"]
doorsList = ["2", "3", "4", "5more"]
personsList = ["2", "4", "more"]
lug_bootList = ["small", "med", "big"]
safetyList = [ "low", "med", "high"]
clssList = ["unacc", "acc", "good", "vgood"]

buyingValues = []
maintValues = []
doorsValues = []
clssValues = []
personsValues = []
lug_bootValues = []
safetyValues = []


while (cars != ""):

    foo = ( [pos for pos, char in enumerate(cars) if char == ","])
    at1 = cars[0:foo[0]]
    at2 = cars[foo[0]+1:foo[1]]
    at3 = cars[foo[1]+1:foo[2]]
    at4 = cars[foo[2]+1:foo[3]]
    at5 = cars[foo[3]+1:foo[4]]
    at6 = cars[foo[4]+1:foo[5]]
    clss = cars[foo[5]+1:-1]

    i = 0
    
    for i in range(4):
        if (at1 == buyingList[i]):
            at1 = i
            buyingValues.append(at1)
        if (at2 == maintList[i]):
            at2 = i
            maintValues.append(at2)
        if (at3 == doorsList[i]):
            at3 = i
            doorsValues.append(at3)
        if (clss == clssList[i]):
            clss = i
            clssValues.append(clss)

    for i in range(3):
        if (at4 == personsList[i]):
            at4 = i
            personsValues.append(at4)
        if (at5 == lug_bootList[i]):
            at5 = i
            lug_bootValues.append(at5)
        if (at6 == safetyList[i]):
            at6 = i
            safetyValues.append(at6)

    tmp = [at1,at2,at3,at4,at5,at6,clss]
    carsList.append(tmp)
    # print(cars[0:foo[0]] + cars[foo[0]+1:foo[1]] + cars[foo[1]+1:foo[2]]+ cars[foo[2]+1:foo[3]]+ cars[foo[3]+1:foo[4]]+ cars[foo[4]+1:foo[5]]+ cars[foo[5]+1:])
    # print(foo)
    cars = file.readline()
# print(carsList)

# print("Training entries: {}, labels: {}".format(len(carsList), len(train_labels)))
 

def build_net(n_features, n_classes):
    Dic = {}

    buying = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
    Dic["buying"] = buying
    
    maint = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
    Dic["maint"] = maint

    doors = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
    Dic["doors"] = doors

    persons = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
    Dic["persons"] = persons

    lug_boot = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
    Dic["lug_boot"] = lug_boot

    safety = tf.placeholder(dtype=tf.float32, shape=[None, n_features])
    Dic["safety"] = safety

    clss = tf.placeholder(dtype=tf.int64, shape=[None])
    Dic["clss"] = clss

    hidden_layer1 = tf.layers.dense( buying, 10 , activation=tf.nn.sigmoid)
    Dic["layer1"] = hidden_layer1

    out = tf.layers.dense(hidden_layer1, n_classes, name="output")

    one_hot = tf.one_hot(clss, depth=n_classes)

    loss = tf.losses.softmax_cross_entropy(onehot_labels=one_hot, logits=out) 
    Dic["loss"] = loss

    opt = tf.train.GradientDescentOptimizer(learning_rate=0.07).minimize(loss)
    Dic["opt"] = opt

    softmax = tf.nn.softmax(out)
    Dic["softmax"] = softmax

    class_ = tf.argmax(softmax,1)
    Dic["class"] = class_

    compare_prediction = tf.equal(class_, clss)
    accuracy = tf.reduce_mean(tf.cast(compare_prediction, tf.float32))
    Dic["accuracy"] = accuracy
    
    return Dic

#Iniciando
sess = tf.InteractiveSession()

#obtendo o número de features 
n_features = len(carsList[1])

print (n_features)

Dic_cg = build_net(n_features,num_classes)

sess.run(tf.global_variables_initializer())

#definindo o número de épocas
epochs = 2000

for i in range(epochs):
    
    sess.run(Dic_cg["opt"], feed_dict={Dic_cg["buying"]: buyingValues, Dic_cg["maint"]: maintValues, Dic_cg["doors"]: doorsValues, Dic_cg["persons"]: personsValues, Dic_cg["lug_boot"]: lug_bootValues, Dic_cg["safety"]: safetyValues, Dic_cg["clss"]: clssValues})
    
    # a cada 100 épocas o erro é impresso
    if  i % 100 == 0:
        erro_train = sess.run(Dic_cg["loss"], feed_dict={Dic_cg["buying"]: buyingValues, Dic_cg["maint"]: maintValues, Dic_cg["doors"]: doorsValues, Dic_cg["persons"]: personsValues, Dic_cg["lug_boot"]: lug_bootValues, Dic_cg["safety"]: safetyValues, Dic_cg["clss"]: clssValues})
        print("O erro na época", i,"é", erro_train)
        
#após o fim do treino, é calculada a acurácia
acc = sess.run(Dic_cg["accuracy"], feed_dict={Dic_cg["buying"]: buyingValues, Dic_cg["maint"]: maintValues, Dic_cg["doors"]: doorsValues, Dic_cg["persons"]: personsValues, Dic_cg["lug_boot"]: lug_bootValues, Dic_cg["safety"]: safetyValues, Dic_cg["clss"]: clssValues})
print("A accurácia é:", acc)







