# DepreSAR
This repo provides API usage to get responses from a cloud server that enables **depression detection** and **emotional support** through a social assistive robot, developed and maintained by [NTU AIROBO](http://ai.robo.ntu.edu.tw/en/index.php).

Since this research is currently under submission, please get in touch with our team to communicate the cooperation details to obtain full API access.


## System

### Detection Model 
Version: 1.0 <br>
Trained and tested on [DAIC-WOZ](https://dcapswoz.ict.usc.edu/) dataset, created by USC, details can be found in [1][2]

### Response Generation
Version: 1.0 <br>
Use Chain-of-Thought Prompting with GPT models(gpt-3.5-turbo and gpt-4o), providing definitions and instructions for strategies in [ESC](https://github.com/thu-coai/Emotional-Support-Conversation) framework, details can be found in [3]

## Usage
Replace <⋯⋯> in client.py and run 
>python client.py

### Server URL
contact our team for further information

### Parameters
#### request(json)

|  key  |    value    |  
|-------|-------------|
|"lang"| "en" or "zh", |
|"gender"| 0 (for male) or 1 (for female),|
|"occupation":| string, e.g. ,"teacher", |
|"self-assessed score"| int in \[0, 24\], PHQ-8 score ref to: [EN](https://www.childrenshospital.org/sites/default/files/2022-03/PHQ-8.pdf), [ZH](https://www.depression.org.tw/detection/index_04.asp)  |
|"user_id"| int, e.g., 123,|
|"user_name"| string, e.g., "dep_sup_test", |
|"**user_message**"| string, especially input "exit" or "結束對話" to terminate the dialog and obtain depression detection result |
|"**post_time**"| datetime string, format: "%d/%m/%Y %H:%M:%S"|

#### response(json)

|  key  |    value    |  
|-------|-------------|
|"return_message"| string, especially get "根據本系統的評估結果，您的憂鬱傾向偏高/低，⋯⋯" as depression detection result |

## Contact Info
Dr. Li-Chen Fu, mail: <lichen@ntu.edu.tw>


### Reference
[1] Gratch J, Artstein R, Lucas GM, Stratou G, Scherer S, Nazarian A, Wood R, Boberg J, DeVault D, Marsella S, Traum DR. The Distress Analysis Interview Corpus of human and computer interviews. InLREC 2014 May (pp. 3123-3128)

[2] DeVault, D., Artstein, R., Benn, G., Dey, T., Fast, E., Gainer, A., Georgila, K., Gratch, J., Hartholt, A., Lhommet, M., Lucas, G., Marsella, S., Morbini, F., Nazarian, A., Scherer, S., Stratou, G., Suri, A., Traum, D., Wood, R., Xu, Y., Rizzo, A., and Morency, L.-P. (2014). “SimSensei kiosk: A virtual human interviewer for healthcare decision support”. In Proceedings of the 13th International Conference on Autonomous Agents and Multiagent Systems (AAMAS’14), Paris

[3] Liu, S., Zheng, C., Demasi, O., Sabour, S., Li, Y., Yu, Z., ... & Huang, M. (2021, August). Towards Emotional Support Dialog Systems. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers) (pp. 3469-3483).
