# Attention-from-scratch
どの本や記事を読んでもAttentionの実装は無くて、スクラッチからのカスタムレイヤー実装も乗っていない。<br>
(2023/8/16訂正、詳解ディープラーニング, つくりながら学ぶ! PyTorchによる発展ディープラーニングなどの本(いずれもマイナビブックス)には<br>Attentionの実装が載っていました。そちらも併せて読むといいと思います。)(というか、リポジトリを作り始めて日本語での解説本があることに気づきました。勉強不足でした。なのでこのリポジトリでは学生の観点から"実装する時に"疑問点が残らないように書いたつもりではあります。)<br>
そんな現状に憤りを感じた大学学部三年生が暇な夏休みの時間を使って<br>Pytorchの基本的な仕様とAttentionの実装を行うリポジトリです。<br>
<br>
理論の説明だとか、実装だとかで不正確、非効率なことを書いているかもしれません。GithubやX(@Takanas0517)にコメントをください。<br>
<br>
2023/8/14 Pytorch基本編のPytorch_command.ipynbが細かい手直しはありますが完成しました!<br>
Attention編はお待ちください！<br>
2023/8/22 前のリポジトリに問題点が発生したため再度作り直しました！是非こちらの方をcloneするようにお願いします！<br>
<br>

### 内容
##### pytorch_command.ipynb

- Pytorchの基本コマンド: なるべく覚えておいて欲しいところを書きました。<br>
- DataLoaderの定義: 業務とかで使う時は自分でデータを集めて、自分でデータローダーを定義しなきゃいけないので書きました。<br>
- モデル定義: 最終目標がAttentionの自前実装なのでここからはかなり詳しく書きました。<br>ReLU, Linear(Dense), CNNの自作実装の仕方, パラメータが内部でどう管理されているか、なども書きました
- Appendix: かなり詳しく書きました。モデル定義で書ききれなかったBatchNormalization, Dropout, RNN, LSTMの自作実装や、日本語記事では多分ほぼ初(観測範囲内)の自作Optimizerの定義の仕方とかも書きました。
- Appendix2: 実はPytorchは普通の最適化にも使えるよって話をしました。
- GithubのPreviewだとipynbのmarkdown部分がうまく表示されない場合がありますが、Cloneして手元のVSCodeで開けば綺麗に映るはずです。<br>

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
鋭意製作中(目標2023/8/24までに公開)
