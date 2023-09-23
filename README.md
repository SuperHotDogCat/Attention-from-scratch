# Attention-from-scratch
どの本や記事を読んでもAttentionの実装は無くて、スクラッチからのカスタムレイヤー実装も乗っていない、そんな現状に憤りを感じた大学学部三年生が暇な夏休みの時間を使ってPytorchの基本的な仕様とAttentionの実装を行うリポジトリです。<br><br>
(2023/8/16訂正、詳解ディープラーニング, つくりながら学ぶ! PyTorchによる発展ディープラーニングなどの本(いずれもマイナビブックス)にはAttentionの実装が載っていました。そちらも併せて読むといいと思います。)(というか、リポジトリを作り始めて日本語での解説本があることに気づきました。勉強不足でした。なのでこのリポジトリでは学生の観点から"実装する時に"疑問点が残らないように書いたつもりではあります。)<br>

理論の説明だとか、実装だとかで不正確、非効率なことを書いているかもしれません。Githubにコメントをください。<br>
<br>

### 内容
上から順に読むことを想定しています。
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

##### GPT_from_scratch.ipynb
- GPT1の制作の解説をしました。GPT2やGPT3のようにZero shotやFew shot機能はないです
- GPTの構造の説明、レイヤーの実装
- Hugging Faceからトークナイザー, openwebtextデータのダウンロード、前処理方法解説
- CPUのメモリに乗せるとクラッシュするデータをnp.memmapで処理する方法
- 学習は失敗しました。

##### Improved_GPT.ipynb
- GPT_from_scratch.ipynbでの問題点解説、改良
- 最後にデモ例として一番良かった学習結果を載せてある。
  
##### learning_notes.ipynb
- GPTの学習中に発生したトラブルの解決策の解説
- さらにAdvancedなPytorchの使い方をまとめた。
  
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
ライブラリ環境　requirements_ubuntu.txt, requirements_gpt.txt<br>

以下感想&自分語り

# 俺の大学三年の夏休みは自然言語に消えてしまった。
- 次回はint64の128×1024テンソルとかをガンガン流して計算グラフ構築しても大丈夫そうな40〜80GBGPUを回せる環境を手に入れたらリベンジします。

#### 敗因まとめ
- モデルがGPUに乗ったとしても計算の途中で計算グラフやら変数やらが暗黙に構成されてクソ重くなるので8GBのGPUではまず足りなかった<br>
- 学習する時の文のサイズは長ければ長いほど汎化性能がよくなり、1024以上で安定して損失が減っていくのはわかったが、<br>貧弱GPUではバッチサイズが6しか確保出来ず、汎化性能が良くなかった(実はこれは勾配累積で解決できた。)
- 突然損失が増大することがあった、これはどうもLLMを学習してるとよくあることらしい
- cos schedulerを使ったんスけど、本当に効果あったんか？これ
- # パソコンが2週間ずっと計算しててま〜〜〜〜じでせっかくのPCなのにゲームが全くできなかった‼️
#### やって良かったと感じたこと
- float32じゃ重すぎるから適宜演算にbfloat16に切り替えると演算がGPUに乗ることとかがわかって楽しかった
- CUDAの機能に少し詳しくなれた
- ぶっちゃけもうTransformer組むのに抵抗感は無い
- GPUがさらに欲しくなった、身体はV100, A100, H100を求める
- 大学での授業を割と総動員して取り組めた感じはあった、勉強したことは無駄ではない
