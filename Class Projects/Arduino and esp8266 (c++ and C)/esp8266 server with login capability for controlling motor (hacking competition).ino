#include <ESP8266WiFi.h>
#include <WebSockets4WebServerSecure.h>
#include <Stepper.h>
#include <Keypad.h>
#include <crypto.h>

// change this to the number of steps on your motor
#define STEPS 200
#define IN1 5
#define IN2 4
#define IN3 14
#define IN4 12

const int stepsPerRevolution = 200; 
Stepper myStepper(STEPS, IN1, IN2, IN3, IN4);

//static const uint8_t D0   = 16;
//static const uint8_t D1   = 5;
//static const uint8_t D2   = 4;
//static const uint8_t D3   = 0;
//static const uint8_t D4   = 2;
//static const uint8_t D5   = 14;
//static const uint8_t D6   = 12;
//static const uint8_t D7   = 13;
//static const uint8_t D8   = 15;
static const uint8_t RX   = 3;
//static const uint8_t D10  = 1;
const byte n_rows = 4;
const byte n_cols = 4;
 
char keys[n_rows][n_cols] = {
  {'1','2','3','2'},
  {'4','5','6','0'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
 
byte colPins[n_rows] = {D7, D8, RX, 10};
byte rowPins[n_cols] = {D0, D3, D4, 9};
 
Keypad myKeypad = Keypad( makeKeymap(keys), rowPins, colPins, n_rows, n_cols); 

//
const char* ssid="Joshua";
const char* password="ckhw5168";
int LED=2;
int websockMillis=50;

unsigned long startMillis;  //some global variables available anywhere in the program
unsigned long currentMillis;
const unsigned long period = 1000*5;  // refresh time

bool flagContent = 0;

unsigned int counter=random(0000,9999);
unsigned int counter2 = 0;
unsigned int failed_attempts=0;
unsigned long lastMillis=millis();



BearSSL::ESP8266WebServerSecure server(443);
WebSockets4WebServerSecure webSocket;
String webSite,JSONtxt;
boolean LEDonoff=true;

char webSiteCont[2000];

struct experimental::crypto::SHA256 SHA256;

static const char serverCert[] PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
MIIDqjCCApKgAwIBAgIUJWNY9lDgwFFWMdqnXerN9+JU/AEwDQYJKoZIhvcNAQEL
BQAwXDELMAkGA1UEBhMCVVMxCzAJBgNVBAgMAkxBMQ8wDQYDVQQHDAZSdXN0b24x
FTATBgNVBAoMDENsdWIgUGVuZ3VpbjEYMBYGA1UEAwwPMTkyLjE2OC4yMTIuMTYy
MB4XDTIzMDIxNDExMjgzMVoXDTM0MDUwMzExMjgzMVowXDELMAkGA1UEBhMCVVMx
CzAJBgNVBAgMAkxBMQ8wDQYDVQQHDAZSdXN0b24xFTATBgNVBAoMDENsdWIgUGVu
Z3VpbjEYMBYGA1UEAwwPMTkyLjE2OC4yMTIuMTYyMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEArW2duk201OCUvrfQgYgc/ZpBvMPNZmU4aTRyN492HFRm
4pf62TXp1VwaEELI/OFOYw40Ty1zegy95XALHQdFFXv8PqnAQiNHMAl0RBmZh9cR
loLFJLBjPlExV4/N2VkyHbeSkJYx1iJ/6klAOMXqh+W+qHxGRdp4RHfiIv6Gsrwg
jfxOpFyot1p8lDpPzBSbxEMWNt/r5SXo5DrHC1ytfpKU+le/nhYJwR7NJeZ9jfIw
K7yI7s4xwX6Z0YG13yDNRBrZ4nl4Dnrj1QaQ5PcSYhfM1MfTK6Yk0Rb9Bkv/Wktf
5cYP1lpF9Wx5wLUSBMW70Mkf+Ia0N3joXK+k8dxeowIDAQABo2QwYjAdBgNVHQ4E
FgQUHYRyASAlNN6XIJv9ztSuyV9UdNowHwYDVR0jBBgwFoAUHYRyASAlNN6XIJv9
ztSuyV9UdNowDwYDVR0TAQH/BAUwAwEB/zAPBgNVHREECDAGhwTAqNSiMA0GCSqG
SIb3DQEBCwUAA4IBAQAFGp/rstJQdxX3HuWc+SmVf+DTQagLeYSiPpq1rtfly9zC
DmPX/XYhEzrDOrHJ7RiRWGBS64RVF0HkgYsRLMS5VianJbSVVyeAOLBfu7/AjlOY
kR4RajpzCzlE7/7mzcRhCLmw8By/sSFH3CMT18m46x6ywbvBRCo50mxGYhtG+VPj
taDhXIzFijbq4YWYU6Kcb/gKmep0UM3xaMTxkzbq1BRy00tVF874YrAThNJWxp0k
ZmqbnzKKMRyYDWFlawpiJ/1zVDlhSKlHtlYo05VD9Nz5uPTjECeCtJDyY3LwOyxe
E9J6Z0Ic6LD2oS8k67VVHSwBNmkwMMZV5mevfwV1
-----END CERTIFICATE-----
)EOF";

static const char serverKey[] PROGMEM = R"EOF(
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCtbZ26TbTU4JS+
t9CBiBz9mkG8w81mZThpNHI3j3YcVGbil/rZNenVXBoQQsj84U5jDjRPLXN6DL3l
cAsdB0UVe/w+qcBCI0cwCXREGZmH1xGWgsUksGM+UTFXj83ZWTIdt5KQljHWIn/q
SUA4xeqH5b6ofEZF2nhEd+Ii/oayvCCN/E6kXKi3WnyUOk/MFJvEQxY23+vlJejk
OscLXK1+kpT6V7+eFgnBHs0l5n2N8jArvIjuzjHBfpnRgbXfIM1EGtnieXgOeuPV
BpDk9xJiF8zUx9MrpiTRFv0GS/9aS1/lxg/WWkX1bHnAtRIExbvQyR/4hrQ3eOhc
r6Tx3F6jAgMBAAECggEAZiVR6RErmNZNxabuH9zTdmsMnOmWaODlQNGrFB5jKnxr
vLpW/OhMOWZt03YCey8YxC7xkFDs2s32atR7NzW48tZ700yX+Fxe6WQoHpQVYXTC
3ytWgi2Bxop7zV7dl055vhcJNC/CWqUnQg6yzL2FTVV73jCUE0CB5ZHWl1XicBJ1
qUx9rKhRRh6plfO/BbCjP7bHxq54XNe4PkE1csP1HYfb2cfcAywuH8uxoIPHk6ci
wBsdqe/UES8eNeBd5SmEq68NB/EJaY/29qCf57N55aSrYVxeiDKs/WjmYDvyP8yP
9tXhZCBY9Dd4oYsETUcVJO1eUS19SCmwTzYWkMJEQQKBgQDY/Qj1BFwj/BgGYKoN
niM02wDUGZnf9dV3bwy/nDcQ5Dk9vs+3vpsMSgXM+GgpsVqcdcp5g9goBt0lGgvD
3rZT4U0+k1fLAXmLyqdHDREHF5uYx3FXFentkQo0g5Nz0n/kPF/SSfsg7lJB980F
j2l+GiLOTzlFlfgBXQ8DRjwNnQKBgQDMm7T2Pdwilh7Bniw2jOrRE2z49zC5Wy21
zv7jznsj8QLZQ61zWKlM3XxQXzmeQFkIjBkE03JqteMykxK0J0+CUW3H780KhR39
vzF0+f3ovlFuvwcBi8dt845FL+ItpdU/QqRr9bs3x5cijiXtawt45gNObzudfurN
DDZtGTyJPwKBgA82tpEPTDKNs1WHI4Uu6EMFc+prHRnRz7S/CYLJviamCcllfoTg
jVhwPDXh2NPLhpHfxGF+uAIecRTv3ZFPJTN+YX8Yr5ghM1d0zwOxS9dWdWdh3HWB
qNQqTi/eZdFCGgtznDhPTZdCfmv3pt1T786SoIwci+RwHmJiFvJg00cVAoGBAJQH
5zHsaXLgd5oPTN+erljbnBC4DplcHUMXYpQAlFjZiv0TmM8GC17gM4uWiYIz/fZQ
Hd2++V25AIpbm8GZW03mie2IUilVS/CEvkxqfchAwXvFW1VEAuJKvtjRnur1usXM
+lZdb7kYfwDyJQCTXLZ4e1Xo5hG5fDkjp9Dg3EpTAoGBAIldGy1FMIVYyjHXnMRi
+bzujlYB5PGzZCLgF+TSV7C4NXeeiAeHgDZFlFgkQqJ3NwRS+CM1bVTWzmkvPcMp
yJh1E5Xkvrs1heoH7PNUbkqZw2UiuamKTCtcRse4M/etuGe6EhTuv4VV8Qa4tnMk
sXkCViqz3YyXZmQWg1tsyF9/
-----END PRIVATE KEY-----
)EOF";  

char webSiteCont1[] = 
R"=====(

<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<style>
body  
{  
    margin: 0;  
    background-color:Cyan;  
    font-family: 'Arial';  
}  
.login
{  
  width: 282px;  
  overflow: hidden;  
  margin: auto;  
  margin: 20 0 0 0px;  
  padding: 60px;  
  background: SeaGreen;  
  border-radius: 100px ;          
}  
h2{  
    text-align: center;  
    color: SeaGreen;  
    padding: 10px; 
    font-size: 75px;
    font-family: Courier New;
}  
label{  
    color: Cyan;  
    font-size: 17px;  
}  

#Pass{  
    width: 275px;  
    height: 30px;  
    border: none;  
    border-radius: 100px;  
    padding-left: 8px;  
      
}  

#username{  
    width: 275px;  
    height: 30px;  
    border: none;  
    border-radius: 100px;  
    padding-left: 8px;  
      
}  
#log{  
	background: White;
    width: 100px;  
    height: 30px;
    margin-left:100px;
    border: none;  
    border-radius: 17px;  
    color: SeaGreen;
}  
</style>
<body>
    <h2>CLUB PENGUIN</h2><br>
    <div class="login">
    <div id="login" >
    <label><b>Username</b></label>
      <input type="text" name="username" id="username">
      <br>
      <label><b>Password</b></label>
      <input type="Password" name="Pass" id="Pass">
      <br><br>
      <button onclick="sendPass()" id="log" > Log in </button>
    </div>     
</div>
</body>
<SCRIPT> 
 InitWebSocket()
  function InitWebSocket()
  {
    websock = new WebSocket('wss://'+window.location.hostname+':443/');
  } // end of InıtWebSocket
   function sendPass(){
    var stringPass=document.getElementById("Pass").value; 
    var stringusername=document.getElementById("username").value;
    var Password = 'Pass='+stringPass+',username='+stringusername; 
     //alert(stringPass);
    websock.send(Password);
    location.reload();
    } 
</SCRIPT>

)=====";

char webSiteCont2[]  = 
R"=====(

<!DOCTYPE HTML>
<HTML>
<META name='viewport' content='width=device-width, initial-scale=1'>

<SCRIPT>

  InitWebSocket()
  function InitWebSocket()
  {
    websock = new WebSocket('wss://'+window.location.hostname+':443/');
    websock.onmessage=function(evt)
    {
       JSONobj = JSON.parse(evt.data);
       document.getElementById('btn').innerHTML = JSONobj.Data;
    } // end of onmessage
      
  } // end of InıtWebSocket
  
  setInterval(function(){ location.reload();},1000*5);


</SCRIPT>

<style> 
#btn{
    position:relative;
    top:200px;
    width: 300px;
    margin: auto;  
    font-size: 100px;
  }
</style>

<BODY>
  <div id="btn"> </div>

</BODY>

</HTML>

)=====";

//motor wepage here
char webSiteCont3[]  = 
R"=====(
<!DOCTYPE html>
<html>
<head>
    <title>Login Form</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<style>
body
{
    margin: 0;
    background-color:Cyan;
    font-family: 'Arial';
}
.login
{
  width: 282px;
  overflow: hidden;
  margin: auto;
  margin: 20 0 0 0px;
  padding: 60px;
  background: SeaGreen;
  border-radius: 100px ;
}
h2{
    text-align: center;
    color: SeaGreen;
    padding: 10px; 
    font-size: 75px;
    font-family: Courier New;
}
label{
    color: Cyan;
    font-size: 17px;
}

#Pass{
    width: 275px;
    height: 30px;
    border: none;
    border-radius: 100px;
    padding-left: 8px;

}

#username{
    width: 275px;
    height: 30px;
    border: none;
    border-radius: 100px;
    padding-left: 8px;

}
#log{
    background: White;
    width: 100px;
    height: 30px;
    margin-left:100px;
    border: none;
    border-radius: 17px;
    color: SeaGreen;
}
</style>
<body>
    <h2>Motor Power</h2><br>
    <div class="login">
    <div id="login" >
    <label><b>Click Here to Power Off</b></label>
      <br><br>
      <button onclick="sendPass()" id="log" > Power Button </button>
    </div>
</div>
</body>
<SCRIPT> 
 InitWebSocket()
  function InitWebSocket()
  {
    websock = new WebSocket('wss://'+window.location.hostname+':443/');
  } // end of InıtWebSocket
   function sendPass(){
    var Password = 'Poweroff'; 
    websock.send(Password);
    location.reload();
    } 
</SCRIPT>
)=====";//end motorpage

void WebSite(){

  server.send(200,"text/html",webSiteCont);
  
}

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t welength)
{
  String payloadString = (const char *)payload;
  Serial.print("payloadString= ");
  Serial.println(payloadString);

  if(type == WStype_TEXT) // receive text from cliet
  {
    int separator=payloadString.indexOf(',');
    String var1 = payloadString.substring(0,separator);
    String var2 = payloadString.substring(separator+1,payloadString.length());
    
    Serial.print("var1=");
    Serial.println(var1);
    Serial.print("var2=");
    Serial.println(var2);

    separator=var1.indexOf('=');
    String val1 = var1.substring(separator+1,var1.length());
    separator=var2.indexOf('=');
    String val2 = var2.substring(separator+1,var2.length());

    Serial.print("val1=");
    Serial.println(val1);
    Serial.println(" ");
    Serial.print("val2=");
    Serial.println(val2);
    Serial.println(" ");
    String val1Hash = SHA256.hash(val1); String val2Hash = SHA256.hash(val2);    
    if(val1Hash == "c142d2924713a608ca8bae52c338d689f99c2e99c2fd8fb3c078b3e7cda8ec26"/*clubpeng*/ && val2Hash == "02d08359f754fb6b3afcf916e7784a2a41eb8196f5c43d647e368aeb0ad47597"/*erik*/ && (failed_attempts <= 5))
    {
        Serial.println("switch screen"); 
        //String str = "hello world";
        myStepper.step(stepsPerRevolution);
        size_t sizeStr = sizeof(webSiteCont2) / sizeof(webSiteCont2[0]);
        //Serial.println(sizeStr); 
        memcpy(webSiteCont,webSiteCont2 , sizeStr);
        flagContent = 1;
        startMillis = millis();  //initial start time 
        //str.toCharArray(webSiteCont,3);
    } 

    else if (val1 == "12345" && val2 == "andrew" && (failed_attempts <= 5))
    {
        Serial.println("switch screen"); 
        //String str = "hello world";
        myStepper.step(stepsPerRevolution);
        size_t sizeStr = sizeof(webSiteCont3) / sizeof(webSiteCont3[0]);
        //Serial.println(sizeStr); 
        memcpy(webSiteCont,webSiteCont3 , sizeStr);
        flagContent = 1;
        startMillis = millis();  //initial start time 
    } 
    else
    {
      failed_attempts++;
      Serial.print("Number of failed attempts="); 
      Serial.println(failed_attempts); 

    }  
  } 
}

int keyArray[4];
int i = 0;


void setup() {
  myStepper.setSpeed(60);
  Serial.begin(9600);
  size_t sizeStr = sizeof(webSiteCont1) / sizeof(webSiteCont1[0]);
  Serial.println(sizeStr); 
  sizeStr = sizeof(webSiteCont2) / sizeof(webSiteCont2[0]);        
  Serial.println(sizeStr); 
  memcpy(webSiteCont, webSiteCont1, (sizeStr+1300));
        
  pinMode(LED,OUTPUT);
  WiFi.begin(ssid,password);
  while(WiFi.status() != WL_CONNECTED)
  {
    Serial.println(".");
    delay(500);  
  }

  //set cert and key
  server.getServer().setRSACert(new BearSSL::X509List(serverCert), new BearSSL::PrivateKey(serverKey));
  
  WiFi.mode(WIFI_STA);
  Serial.println(" Start ESP ");
  Serial.println(WiFi.localIP());
  server.on("/",WebSite);
  server.addHook(webSocket.hookForWebserver("/wss", webSocketEvent));
  server.begin();
  

}

void loop() {
  

 webSocket.loop();
 server.handleClient();
      
  if( flagContent == 1 )
  {
      currentMillis = millis();  //get the current "time" (actually the number of milliseconds since the program started)
      if (currentMillis - startMillis >= period)  //test whether the period has elapsed
      {
    
      Serial.println("switch screen"); 
      size_t sizeStr = sizeof(webSiteCont1) / sizeof(webSiteCont1[0]);
      memcpy(webSiteCont,webSiteCont1 , sizeStr);
      flagContent = 0;
      startMillis = currentMillis;  //IMPORTANT to save the start time of the current LED state.
      }
  }

  //update every minute 
  currentMillis = millis();
  if ((currentMillis-lastMillis)>=60000)
  {
    counter=random(0000,9999);
    lastMillis=millis();
    Serial.println( counter );
  }
  
  
  if( flagContent == 1 )
  {
    String Data = String(counter);
    JSONtxt = "{\"Data\":\""+Data+"\"}";
    webSocket.broadcastTXT(JSONtxt);
  }

  char myKey = myKeypad.getKey();
  
 
  if (myKey != 0){
    Serial.print("Key pressed: ");
    Serial.println(myKey);

    if (myKey != 35){
      keyArray[i] = (myKey-48);
      int a = (myKey-48);

       i+=1;

    }

    else{
      
      for (int x = 0; x < 4; x++){
        keyArray[x] = 0;
      }

      i = 0;
    }    
  }

  int number;
  if (number == counter){
    
    Serial.println("YOU DID IT");
  }
  for (int x = 0; x < 4; x++){
    
    number += keyArray[x]*(1000/pow(10,x));
    
  }
  //Serial.println(number);
  if (number == counter){
    Serial.println("Equal");
  }
  else {
    //Serial.println("not equal");
  }

  


}
