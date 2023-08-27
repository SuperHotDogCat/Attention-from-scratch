# Attention-from-scratch
どの本や記事を読んでもAttentionの実装は無くて、スクラッチからのカスタムレイヤー実装も乗っていない、そんな現状に憤りを感じた大学学部三年生が暇な夏休みの時間を使ってPytorchの基本的な仕様とAttentionの実装を行うリポジトリです。<br><br>
(2023/8/16訂正、詳解ディープラーニング, つくりながら学ぶ! PyTorchによる発展ディープラーニングなどの本(いずれもマイナビブックス)にはAttentionの実装が載っていました。そちらも併せて読むといいと思います。)(というか、リポジトリを作り始めて日本語での解説本があることに気づきました。勉強不足でした。なのでこのリポジトリでは学生の観点から"実装する時に"疑問点が残らないように書いたつもりではあります。)<br>

理論の説明だとか、実装だとかで不正確、非効率なことを書いているかもしれません。GithubやX(@Takanas0517)にコメントをください。<br>
<br>

### 内容
##### pytorch_command.ipynb

- Pytorchの基本コマンド: なるべく覚えておいて欲しいところを書きました。<br>
- DataLoaderの定義: 業務とかで使う時は自分でデータを集めて、自分でデータローダーを定義しなきゃいけないので書きました。<br>
- モデル定義: 最終目標がAttentionの自前実装なのでここからはかなり詳しく書きました。<br>ReLU, Linear(Dense), CNNの自作実装の仕方, パラメータが内部でどう管理されているか、なども書きました
- Appendix: かなり詳しく書きました。モデル定義で書ききれなかったBatchNormalization, Dropout, RNN, LSTMの自作実装や、日本語記事では多分ほぼ初(観測範囲内)の自作Optimizerの定義の仕方とかも書きました。
- Appendix2: 実はPytorchは普通の最適化にも使えるよって話をしました。
- GithubのPreviewだとipynbのmarkdown部分がうまく表示されない場合がありますが、Cloneして手元のVSCodeで開けば綺麗に映るはずです。<br>

##### attention_from_scratch.ipynb
- Attention誕生の経緯: 何故Attentionなのかを簡単に述べました
- Self-Attention, MultiheadAttention, Transformerの簡単な理論と実装上の注意、実装例:　実装の際に気をつけることに絞って簡単に数式を用いて解説を行いました。
- Attention機構を用いた日英翻訳タスクの例: Hugging Faceからデータを取ってきて実際に翻訳タスクを行いました。

##### BERT.ipynb(BERTの実装を行うipynbを制作するかも。。。？)
制作環境<br>
pytorch_command.ipynb<br>
MacBook Air<br>
チップ Apple M1<br>
メモリ 16GB<br>
OS Ventura 13.4<br>
Python3.8.8<br>
ライブラリ環境　requirements_mac.txt<br>
<br>
attention_from_scratch.ipynb<br>
CPU : インテル® Core™ i7-13650HX<br>
GPU : NVIDIA® GeForce RTX™ 4060 Laptop GPU 8GB<br>
メモリ : 32GB<br>
OS : Ubuntu 22.04.3 LTS<br>
Python 3.10.12<br>
ライブラリ環境　requirements_ubuntu.txt<br>
