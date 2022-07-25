### How to run
### requirements:
1. Flask (python library installed with pip)
2. ngrok (CLI tool, with homebrew use `brew install ngrok/ngrok/ngrok`)
   1. Create account for ngrok and add activation code to CLI using `ngrok config add-authtoken ......`

### how to run

1. inside this folder, run `flask run`
2. then run `ngrok http 127.0.0.1:5000/` (localhost and port for flask api running)
3. ngrok will give you a public URL that can be used in the integration to listen to different events, something like " https://c631-88-92-175-248.eu.ngrok.io".

NOTE: Ngrok urls are blocked on the internal cisco net, but can still be used by the workspace integration.