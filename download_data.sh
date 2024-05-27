#!/bin/bash
curl 'https://ocws.officeapps.live.com/ocs/v2/recent' \
  -H 'accept: */*' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCIsImtpZCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCJ9.eyJhdWQiOiJodHRwczovL29mZmljZWFwcHMubGl2ZS5jb20iLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC80ODIxOThiYi1hZTdiLTRiMjUtOGI3YS02ZDdmMzJmYWEwODMvIiwiaWF0IjoxNzE2NzQ2NTM4LCJuYmYiOjE3MTY3NDY1MzgsImV4cCI6MTcxNjgzMzIzOCwiYWNyIjoiMSIsImFpbyI6IkFTUUEyLzhXQUFBQTFwcG1rdXRLeFE0U1pKc0dMQUJPc3o5TXlzMjR5dHpnT0Jhd1Y0cjF0ZVU9IiwiYW1yIjpbInB3ZCJdLCJhcHBpZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMCIsImFwcGlkYWNyIjoiMiIsImF1dGhfdGltZSI6MTcxNjA2ODM0MiwiZmFtaWx5X25hbWUiOiJIYWxsIiwiZ2l2ZW5fbmFtZSI6IkJlbmFqbWluIiwiaXBhZGRyIjoiMjYxMDoxNDg6MWYwMjo3MDAwOmYyNGU6YjZjMDozZWJkOmU2YzkiLCJuYW1lIjoiSGFsbCwgQmVuYWptaW4iLCJvaWQiOiI3MDRlMmVhYi01ZGY3LTRjYjctOTAwZC1jYzcyMzE1NzFkNzUiLCJvbnByZW1fc2lkIjoiUy0xLTUtMjEtMTE3NzIzODkxNS0yMTExNjg3NjU1LTEwNjAyODQyOTgtMTcxMzE0OSIsInB1aWQiOiIxMDAzMjAwMkI3MzRFMkQ5IiwicmgiOiIwLkFUZ0F1NWdoU0h1dUpVdUxlbTFfTXZxZ2c5U05hUThSOENOTm96NnpaQmJjc2VZNEFPby4iLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJzdWIiOiJaX3NHUklMT2FNQUJIdXhackhiTnF4VkFWckcxajdyTUhqdFlVYjFpb3pNIiwidGlkIjoiNDgyMTk4YmItYWU3Yi00YjI1LThiN2EtNmQ3ZjMyZmFhMDgzIiwidW5pcXVlX25hbWUiOiJiaGFsbDc1QGdhdGVjaC5lZHUiLCJ1cG4iOiJiaGFsbDc1QGdhdGVjaC5lZHUiLCJ1dGkiOiJQMkZuRUFHTXNFdVFxeEFld2VhbUFBIiwidmVyIjoiMS4wIn0.CTA-MXwEyJ2mfgxIc5UJQ9KH_KeAfBACl61GbXwklxdRHLzKnAfpIihcKMnC7R6geAgX598UKlmTb_dGJ8jNG7Ok6CJd-ZJR3BReNvji58m3ePHOt99gkB05L2BYKj5MLwIQBqL5rFjXbVDqRhr8b7bB4muHpkRfjGWvXlb_MvbBncjcv5S0t8te4iU4kYTYcBKlKYybxyICm91dVRmiYncBfwxbM7imEC0Vbzdp6kogFCs3TAQjD01SU1ECd0iUvQJtPYyNnWlXo6XH6jiG91KX1pVLX4ocFfH-EQ4RBPIiptJxiyp7Cly2zrjMzq9FQInkwdewYxE2zrNZVwEPcw' \
  -H 'content-type: application/json;charset=UTF-8' \
  -H 'dnt: 1' \
  -H 'origin: https://gtvault.sharepoint.com' \
  -H 'referer: https://gtvault.sharepoint.com/' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: cross-site' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -H 'x-office-application: 110' \
  -H 'x-office-platform: Web' \
  -H 'x-office-version: odsp-web-prod_2024-05-10.008' \
  --data-raw $'{"category":"Document","type":"DocumentUrl","app":"OtherNonOffice","url":"https://gtvault.sharepoint.com/sites/HyTechRacing2/Shared%20Documents/Electrical%20-%20Data-Acquisition/VEHICLE%20DATA/HT08","title":"HT08","onedrive_info":{"drive_id":"b\u0021Xj4BYu-gOUubhIFWpOBOP56lhHiO6SpMpVZkv6NUaeigz3A_cjW2R6WzWiQ5uRck","item_id":"01KTWB5X5SVT6V24MOOVEIN3X7XA4IYPTU"},"resource_id":"01KTWB5X5SVT6V24MOOVEIN3X7XA4IYPTU","sharing_info":{"state":0},"display_path":["Shared Documents","Electrical - Data-Acquisition","VEHICLE DATA"],"sharepoint_info":{"list_id":"3f70cfa0-3572-47b6-a5b3-5a2439b91724","list_item_id":47019,"list_item_unique_id":"5dfdacb2-8e71-4875-86ee-ffb8388c3e74","site_id":"62013e5e-a0ef-4b39-9b84-8156a4e04e3f","site_url":"https://gtvault.sharepoint.com/sites/HyTechRacing2","tenant_id":"482198bb-ae7b-4b25-8b7a-6d7f32faa083","web_id":"7884a59e-e98e-4c2a-a556-64bfa35469e8"}}'


curl 'https://eastus1-mediap.svc.ms/transform/zip?cs=fFNQTw' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cache-control: max-age=0' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'dnt: 1' \
  -H 'origin: https://gtvault.sharepoint.com' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: iframe' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: cross-site' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  --data-raw 'zipFileName=HT08.zip&guid=c4b8f46d-4ee7-4931-bc97-0b94d41defb2&provider=spo&files=%7B%22items%22%3A%5B%7B%22name%22%3A%22HT08%22%2C%22size%22%3A0%2C%22docId%22%3A%22https%3A%2F%2Fgtvault.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb%21Xj4BYu-gOUubhIFWpOBOP56lhHiO6SpMpVZkv6NUaeigz3A_cjW2R6WzWiQ5uRck%2Fitems%2F01KTWB5X5SVT6V24MOOVEIN3X7XA4IYPTU%3Fversion%3DPublished%26access_token%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvZ3R2YXVsdC5zaGFyZXBvaW50LmNvbUA0ODIxOThiYi1hZTdiLTRiMjUtOGI3YS02ZDdmMzJmYWEwODMiLCJjYWNoZWtleSI6IjBoLmZ8bWVtYmVyc2hpcHwxMDAzMjAwMmI3MzRlMmQ5QGxpdmUuY29tIiwiZW5kcG9pbnR1cmwiOiJyeGxPYkdzV3NnZ0YvUVVKazZUa3krMlhTY0ErWGcvbnUwZStUZTZYZ3ZJPSIsImVuZHBvaW50dXJsTGVuZ3RoIjoiMTE0IiwiZXhwIjoiMTcxNjc2ODAwMCIsImlwYWRkciI6IjI2MTA6MTQ4OjFmMDI6NzAwMDpmMjRlOmI2YzA6M2ViZDplNmM5IiwiaXNsb29wYmFjayI6IlRydWUiLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJpc3VzZXIiOiJ0cnVlIiwibmFtZWlkIjoiMCMuZnxtZW1iZXJzaGlwfGJoYWxsNzVAZ2F0ZWNoLmVkdSIsIm5iZiI6IjE3MTY3NDY0MDAiLCJuaWkiOiJtaWNyb3NvZnQuc2hhcmVwb2ludCIsInNpZCI6IjllY2I2ZTFmLTVmZDctNDFkMi1iZmIzLWJiNWY1MmNjYWRjMyIsInNpZ25pbl9zdGF0ZSI6IltcImttc2lcIl0iLCJzaXRlaWQiOiJOakl3TVRObE5XVXRZVEJsWmkwMFlqTTVMVGxpT0RRdE9ERTFObUUwWlRBMFpUTm0iLCJzbmlkIjoiNiIsInN0cCI6InQiLCJ0dCI6IjAiLCJ2ZXIiOiJoYXNoZWRwcm9vZnRva2VuIn0.-HqjyLn6Q9wgGLbNCrtx7X1X7y_WDhOFGn54utF_p9w%22%2C%22isFolder%22%3Atrue%7D%5D%7D&oAuthToken=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCIsImtpZCI6IkwxS2ZLRklfam5YYndXYzIyeFp4dzFzVUhIMCJ9.eyJhdWQiOiJodHRwczovL2Vhc3R1czEtbWVkaWFwLnN2Yy5tcyIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzQ4MjE5OGJiLWFlN2ItNGIyNS04YjdhLTZkN2YzMmZhYTA4My8iLCJpYXQiOjE3MTY3NDY1MzcsIm5iZiI6MTcxNjc0NjUzNywiZXhwIjoxNzE2NzUwODQ0LCJhY3IiOiIxIiwiYWlvIjoiRTJOZ1lEaXVOOUdSWmNmUE5wYkVIcFd3UXUrcHRtdi9xSmFGQ3lyL0NIZFdYbTdZSndFQSIsImFtciI6WyJwd2QiXSwiYXBwX2Rpc3BsYXluYW1lIjoiT2ZmaWNlIDM2NSBTaGFyZVBvaW50IE9ubGluZSIsImFwcGlkIjoiMDAwMDAwMDMtMDAwMC0wZmYxLWNlMDAtMDAwMDAwMDAwMDAwIiwiYXBwaWRhY3IiOiIyIiwiYXV0aF90aW1lIjoxNzE2MDY4MzQyLCJmYW1pbHlfbmFtZSI6IkhhbGwiLCJnaXZlbl9uYW1lIjoiQmVuYWptaW4iLCJpcGFkZHIiOiIyNjEwOjE0ODoxZjAyOjcwMDA6ZjI0ZTpiNmMwOjNlYmQ6ZTZjOSIsIm5hbWUiOiJIYWxsLCBCZW5ham1pbiIsIm9pZCI6IjcwNGUyZWFiLTVkZjctNGNiNy05MDBkLWNjNzIzMTU3MWQ3NSIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xMTc3MjM4OTE1LTIxMTE2ODc2NTUtMTA2MDI4NDI5OC0xNzEzMTQ5IiwicHVpZCI6IjEwMDMyMDAyQjczNEUyRDkiLCJyaCI6IjAuQVRnQXU1Z2hTSHV1SlV1TGVtMV9NdnFnZzlFTFQ1UjdFUnhMcnlhQVR0bGVkbjQ0QU9vLiIsInNjcCI6IlNpdGVzLm1hbmFnZS5BbGwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJoWFNNRDlwTHdHOGZYRndGa3BTbnZ6MVNSRWJiQUFOZlVKdjBPTTcyd0xRIiwidGlkIjoiNDgyMTk4YmItYWU3Yi00YjI1LThiN2EtNmQ3ZjMyZmFhMDgzIiwidW5pcXVlX25hbWUiOiJiaGFsbDc1QGdhdGVjaC5lZHUiLCJ1cG4iOiJiaGFsbDc1QGdhdGVjaC5lZHUiLCJ1dGkiOiJQMkZuRUFHTXNFdVFxeEFldmVhbUFBIiwidmVyIjoiMS4wIn0.VqL_O5SZMKPpSEXe8GdQ5KSK0Ze1FR_nbxZ47RS_4RMPFE8O7ig4V1q0_25S526fGpGnaftXNd1e1TB6Od8U9xt7r-q1p3D9nXD6alTt4NonB6Bl3rcPAcAW9REMn0FfUc8e1FlFIHtjPerxroh-IHXePwQ6Y7A8o-Qz2j5JEdWa6UUoUhIlEPn2Z0Vt2NJs3h9Xgfvj0NKtM67-mNhjb1netIk_uawscbIOx_eBrEZWzlxibF5lbCb654IjHRShGkREWvJSoOM6GJbl8qJ2hs7FQaqv_e6hWF0AxtPjcRhpIiRArqjS99251UnhVb946PioHYKn_gIsseq8Mby97w' --output HT08.zip
