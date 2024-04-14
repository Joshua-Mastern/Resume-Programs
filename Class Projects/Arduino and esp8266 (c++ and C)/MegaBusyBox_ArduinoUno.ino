#include <SPI.h>           // SPI library
#include <SdFat.h>         // SDFat Library
#include <SFEMP3Shield.h>  // Mp3 Shield Library

SdFat sd; // Create object to handle SD functions

SFEMP3Shield MP3player; // Create Mp3 library object
// These variables are used in the MP3 initialization to set up
// some stereo options:

const uint8_t volume = 0; // MP3 Player volume 0=max, 255=lowest (off)
const uint16_t monoMode = 1;  // Mono setting 0=off, 3=max

int denver = 1;
int wrong = 2;
int correct = 3;
int horn = 4;

int musicPin = 36;

const int MAX_LEVEL = 25;
int sequence[MAX_LEVEL];
int your_sequence[MAX_LEVEL];
int level = 1;

int velocity = 1000;

int red = 22;
int redbut =23 ;
int blue = 24;
int bluebut = 25;
int yellow = 26;
int yellowbut = 27;



void setup() {
  
  initSD();  // Initialize the SD card
  initMP3Player(); // Initialize the MP3 Shield

  Serial.begin(9600);
  //simonSays pins
  pinMode(redbut, INPUT);
  pinMode(bluebut, INPUT);
  pinMode(yellowbut, INPUT);
  
  pinMode(red, OUTPUT);
  pinMode(blue, OUTPUT);
  pinMode(yellow, OUTPUT);

  digitalWrite(red, LOW);
  digitalWrite(blue, LOW);
  digitalWrite(yellow, LOW);
  
  Serial.println("start");
}

void loop()
{
  simonSays();
  
  if(digitalRead(musicPin) ==1){
    playSong(denver);
    while(digitalRead(musicPin)==1){
     Serial.print("denver pressed");
     delay(1000);
    }
    Serial.println("leaving loop");
    while(digitalRead(musicPin)==1){
      
    }
  }
}



void playSong(int song)
{
  MP3player.stopTrack();
  MP3player.playTrack(song);
}

void simonSays()
{
  if (level ==1)
    generate_sequence();

  if (level != 1|| digitalRead(redbut)==1)
  {
    delay(1000);
    Serial.println("simon game started");
    Serial.print("red is"); Serial.println(digitalRead(redbut));
    Serial.print("blue is"); Serial.println(digitalRead(bluebut));
    Serial.print("yellow is"); Serial.println(digitalRead(yellowbut));
    show_sequence();
    get_sequence();
  }
}
void show_sequence()
{
  digitalWrite(red, LOW);
  digitalWrite(blue, LOW);
  digitalWrite(yellow, LOW);

  Serial.println("showing sequence now");
  for (int i = 0; i < level; i++)
  {
    Serial.println(sequence[i]);
    digitalWrite(sequence[i], HIGH);
    delay(velocity);
    digitalWrite(sequence[i], LOW);
    delay(200);
  }
  Serial.println("sequence showing done");
}

void get_sequence()
{
    int flag = 0; //this flag indicates if the sequence is correct
    Serial.println("getting player sequence");
    for (int i = 0; i < level; i++)
    {
      if(digitalRead(musicPin) ==1)
      {
          Serial.println("denver music in simon triggered");
          playSong(denver);
          while(digitalRead(musicPin)==1){
          Serial.print("denver music in simon looping");
          delay(1000);

          }
      }
      flag = 0;
      while(flag == 0)
      {   
          delay(100);
          
          if (digitalRead(redbut) == HIGH)
          {
            digitalWrite(red, HIGH);
            your_sequence[i] = red;
            flag = 1;
            delay(200);
            if (your_sequence[i] != sequence[i])
            {
              wrong_sequence();
              return;
            }
            digitalWrite(red, LOW);
          }
          
          if (digitalRead(bluebut) == HIGH)
          {
            digitalWrite(blue, HIGH);
            your_sequence[i] = blue;
            flag = 1;
            delay(200);
            if (your_sequence[i] != sequence[i])
            {
              wrong_sequence();
              return;
            }
            digitalWrite(blue, LOW);
          }
          
          if (digitalRead(yellowbut) == HIGH)
          {
            digitalWrite(yellow, HIGH);
            your_sequence[i] = yellow;
            flag = 1;
            delay(200);
            if (your_sequence[i] != sequence[i])
            {
              wrong_sequence();
              return;
            }
            digitalWrite(yellow, LOW);
          }
      
          
       }
    }
    right_sequence();
}
void generate_sequence()
{
  randomSeed(millis()); //in this way is really random!!!

  for (int i = 0; i < MAX_LEVEL; i++)
  {
    int temprand = random(1, 4);
    int temp;
    if(temprand == 1){
      temp = 22;
    }else if (temprand == 2){
      temp = 24;
    }else if (temprand == 3){
      temp = 26;
    }
    sequence[i] = temp;
  }
}

void right_sequence()
{
  Serial.println("right sequence");
  digitalWrite(red, LOW);
  digitalWrite(blue, LOW);
  digitalWrite(yellow, LOW);
  delay(250);
  
  digitalWrite(red, HIGH);
  digitalWrite(blue, HIGH);
  digitalWrite(yellow, HIGH);
  delay(500);
  
  digitalWrite(red, LOW);
  digitalWrite(blue, LOW);
  digitalWrite(yellow, LOW);

  delay(500);

  if (level < MAX_LEVEL);
    level++;
    
    velocity -= 50; //increase difficulty
}

void wrong_sequence()
{
  Serial.println("wrong sequence");
  for (int i = 0; i < 3; i++)
  {
    digitalWrite(red, HIGH);
    digitalWrite(blue, HIGH);
    digitalWrite(yellow, HIGH);
    
    delay(250);
    digitalWrite(red, LOW);
    digitalWrite(blue, LOW);
    digitalWrite(yellow, LOW);
    delay(250);
  }
  level = 1;
  velocity = 1000;
}

// initSD() initializes the SD card and checks for an error.

void initSD()
{
  //Initialize the SdCard.
  if(!sd.begin(SD_SEL, SPI_HALF_SPEED)) 
    sd.initErrorHalt();
  if(!sd.chdir("/")) 
    sd.errorHalt("sd.chdir");
}

// initMP3Player() sets up all of the initialization for the
// MP3 Player Shield. It runs the begin() function, checks
// for errors, applies a patch if found, and sets the volume/
// stero mode.
void initMP3Player()
{
  uint8_t result = MP3player.begin(); // init the mp3 player shield
  if(result != 0) // check result, see readme for error codes.
  {
    // Error checking can go here!
  }
  MP3player.setVolume(volume, volume);
  MP3player.setMonoMode(monoMode);
}
