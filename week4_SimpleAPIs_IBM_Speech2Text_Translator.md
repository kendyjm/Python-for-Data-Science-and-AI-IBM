---
title: "week4_IBM_Speech2Text_Translator"
author: kjeanmar
date: 24/03/2020
output: html_document
---

https://cloud.ibm.com/login
kendyjm@gmail.com

## https://cloud.ibm.com/services/speech-to-text
`curl -X POST -u "apikey:{apikey}" \
--header "Content-Type: audio/flac" \
--data-binary @{path_to_file}audio-file.flac \
"{url}/v1/recognize"`

`curl -X POST -u "apikey:iNL3YtIwQ61CvEYDanTxvGYvuSehTPx8skRWkc1Gn5-S" --header "Content-Type: audio/flac" --data-binary @audio-file.flac "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/fc2a3f06-39d1-4afe-a6a6-4d12024a17c7/v1/recognize"`

`-bash-4.4$ curl -X POST -u "apikey:iNL3YtIwQ61CvEYDanTxvGYvuSehTPx8skRWkc1Gn5-S" --header "Content-Type: audio/flac" --data-binary @audio-file.flac "https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/fc2a3f06-39d1-4afe-a6a6-4d12024a17c7/v1/recognize"
{
   "results": [
      {
         "alternatives": [
            {
               "confidence": 0.94,
               "transcript": "several tornadoes touched down as a line of severe thunderstorms swept through Colorado on Sunday "
            }
         ],
         "final": true
      }
   ],
   "result_index": 0
}-bash-4.4$`


## https://cloud.ibm.com/services/language-translator