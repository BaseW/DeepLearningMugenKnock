# ディープラーニング∞本ノック!!


ディープラーニング∞本（？）ノックぅぅ

何問になるか分からないので∞本になってます。多分これからいろんな技術が出るからどんどん更新する予定でっす。
これはイモリと一緒にディープラーニングの基礎からDLのライブラリの扱い、どういうDLの論文があったかを実装しながら学んでいくための問題集です。論文読んだだけじゃわからないネットワークの作成や学習率などのハイパーパラメータの設定を自分の手を動かしながら勉強するための問題集です。

- **内容はいろいろな文献を調べて載っけてるので正しくないものもあるかもしれないので注意して下さい**
- 【注意】このページを利用して、または関して生じた事に関しては、私は一切責任を負いません。すべて**自己責任**でお願い致します。

## 環境設定

Python-3.6でやって下さい。(解答はPython-3.6で用意してます)

### 1. Minicondaのインストール

https://conda.io/miniconda.html のサイトからMinicondaをインストールします。これはWindowでもMacOSでも可能です。Minicondaがインストールできたら、端末(Windowでは端末、MacOSではターミナル)を開き、以下コマンドで仮想環境を作成します。

```bash
$ conda create python=3.6 -n dlmugenknock
```

作成できたら、以下コマンドで仮想環境を動作します。

```bash
$ source activate dlmugenknock
```

するとこうなります。

```bash
(dlmugenknock) :~/work_space/DeepLearningMugenKnock/ :$ 
```

### 2. gitのインストール

gitをインストールします。そして、端末を開いて、以下のコマンドを実行します。このコマンドでこのディレクトリを丸ごと自分のパソコンにコピーできます。

```bash
$ git clone https://github.com/yoyoyo-yo/DeepLearningMugenKnock.git
```

### 3. パッケージのインストール

以下のコマンドで必要なパッケージをインストールします。


```bash
$ pip install -r requirements.txt
```

## 問題

詳細な問題内容は各ディレクトリのREADMEにあります。（ディレクトリで下にスクロールすればあります）
- numpy中心ですが、numpyの基本知識は自分で調べて下さい。


### [理論編]()

|番号|問題||番号|問題|
|:---:|:---:|:---:|:---:|:---:|


### [ディープラーニングをやる前の準備編](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_prepare)

|番号|問題|番号|問題|
|:---:|:---:|:---:|:---:|
| 1 | [データセットの読み込み](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_prepare#q2-1-%E5%AD%A6%E7%BF%92%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF) |
| 2 | [ミニバッチの作成](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_prepare#q2-2-%E3%83%9F%E3%83%8B%E3%83%90%E3%83%83%E3%83%81%E4%BD%9C%E6%88%90) |
| 3 | [イテレーション・エポック](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_prepare#q2-3-%E3%82%A4%E3%83%86%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%81%A8%E3%82%A8%E3%83%9D%E3%83%83%E3%82%AF) |
| 4 | [データ拡張・水平反転](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_prepare#q4-%E3%83%87%E3%83%BC%E3%82%BF%E6%8B%A1%E5%BC%B5%E5%B7%A6%E5%8F%B3%E5%8F%8D%E8%BB%A2) |
| 5 | [データ拡張・上下反転](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_prepare#q5-%E3%83%87%E3%83%BC%E3%82%BF%E6%8B%A1%E5%BC%B5%E4%B8%8A%E4%B8%8B%E5%8F%8D%E8%BB%A2) |

### [CNN・フレームワークの使い方編](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_neuralnet)

|番号|問題|
|:---:|:---:|
| 1 | [共通事項](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_neuralnet) |
| 2 | [PyTorch使ったった](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_neuralnet/README_pytorch.md) |
| 3 | [Tensorflow使ったった](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_neuralnet/README_tensorflow.md) |
| 4 | [Keras使ったった](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_neuralnet/README_keras.md) |
| 5 | [Chainer使ったった](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_neuralnet/README_chainer.md) |

### [有名モデル実装編](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_model)

| 番号 | 問題 |  PyTorch | TensorFlow | Keras | Chainer |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | [LeNet](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_model#q1-lenet) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/lenet_pytorch.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/lenet_tensorflow_layers.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/lenet_keras.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/lenet_chainer.py) | 
| 2 | [AlexNet](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_model#q2-alexnet) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/alexnet_pytorch.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/alexnet_tensorflow_layers.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/alexnet_keras.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/alexnet_chainer.py) | 
| 3 | [ZFNet](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/tree/master/Question_model#q3-zfnet) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/zfnet_pytorch.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/zfnet_tensorflow_layers.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/zfnet_keras.py) | [◯](https://github.com/yoyoyo-yo/DeepLearningMugenKnock/blob/master/Question_model/answers/zfnet_chainer.py) | 

### [画像処理編]()

### [言語処理編]()




## TODO

adaptivebinalizatino, poison image blending

