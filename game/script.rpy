
# characters in the game 
define t = Character('Pr. Alfred Stein', color="#FF5733") 
define f = Character('Frank', color="#ffffff") 
define c = Character('Cameron', color="#347B16") 
define a = Character('Anaya', color="#7B3C16") 
define i = Character('Iman', color="#48167B") 
define p = Character('Paloma', color="#EFEC11") 
define m = Character('Marcus', color="#1133EF") 
define d = Character('Demi', color="#EF7611")
define j = Character('Jerome', color="#EF7611")
define u = Character('Unknown Voice', color="#EF7611")

#textbook default
default open_textbook = False

#R background message
default fixed_message = False

#iman screen shot
default screenshot_iman = False

#demi screen shot
default screenshot_demi = False

label start:
# zoom background
scene bg zoom

# player enters her name
$ name = renpy.input("What is your name?")

# the player's character
define you = Character('[name]', color="#0080c0")

#play music "02 Like a Refreshing Sunrise.mp3"

show playerwindowview

show text [name] at truecenter

"I log into the online class session for German 101 held on Zoom. Nine boxes fill the screen."

hide playerwindowview
hide text

scene bg zoomwindows

show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5

show Anaya silent
show Professor silent
show Frank silent
show Cameron silent
show Iman silent
show Paloma silent
show Marcus silent
show Demi silent

show outline Professor
"The white-haired Professor STEIN sits in the upper middle. Followed by the students, all in their early 20s:"

show outline Anaya
"ANAYA - the bored teacher’s assistant,"

show outline Paloma
"Paloma - the hot Latin American foreign exchange student,"

show outline Cameron
"CAMERON - the cool, surfer, heartthrob,"

show outline Marcus
"MARCUS - the class clown,"

show outline Demi
"DEMI - the tomboyish athlete,"

show outline Iman
"IMAN - the South Asian heavy snacker,"

show outline Frank
"FRANK - the brown-noser A+ student,"

show mute_button mute
show outline player
"and me with my video and mic turned off."

hide outline player
hide mute_button mute

$renpy.set_style_preference("choice", "default")
menu:
    "Class begins."

    "Start":
      jump start_class

label start_class:
  you "Another exciting day of German, I can't wait... syke! Kill me now."

  show outline Professor
  t "Do we have everyone Anya?"

  show Anaya talking
  show outline Anaya
  a "It's Anaya. A-NA-YA"

  show Anaya silent
  show outline Professor
  t "Right. Why can’t I see someone’s video? Who is that {color=#0080c0}[name]{/color}?"

  show mute_button unmute
  "I unmute my mic."

  show outline player
  you "Yes ... s-sorry ... my ... camera ... working ... some reason."

  "My audio cuts in and out."

  show outline Anaya
  a "Sounds like [name] is having wifi issues."

  show outline Professor
  t "Fine, fine. In honor of {i}Valentinstag{/i} approaching, today we will be exploring some beautiful German poetry..."

  "Professor Stein drones on and on."
  
  show mute_button mute
  "I mute my mic and let out a sigh of relief. Suddenly my cell phone rings."
  
  # show incoming call photo in top right corner
  show phone_call demi
 

  $renpy.set_style_preference("choice", "default")
  menu:

   "Pick up the phone.":
     jump scene_2

label scene_2:
  hide phone_call demi

  #show facetime
  show facetime demi
  "I pick up the phone, it's ''DEMI'' my best friend who is also in the class."

  d "Hey girl!"

  scene bg zoomwithoutdemi
  show outline Professor
  show Anaya silent
  show Professor silent
  show Frank silent
  show Cameron silent
  show Iman silent
  show Paloma silent
  show Marcus silent
  show facetime demi
  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5

  "She turns off her video in the class so we can talk."

  you "Hey, I guess I was saved by these shitty headphones."
 
  jump choice2

label choice2:
  d "Haha oh I thought you were faking it."

  you "No, my mic actually sucks. Think that's a good enough excuse to leave my camera off too?"

  d "Yeah you can totally {b}leave your camera and mic off for the rest of class{/b}. That's my plan anyways."

  you "Ok good because I can NOT let Cameron see my room. I’ll never live this down."

  d "Come on are you going to hide for the rest of the semester? It can’t be that bad."

  $renpy.set_style_preference("choice", "default")
  menu:

    "No it's even worse than you think":
      jump choice1A

    "Yeah I guess you're right..":
      jump choice1B

label choice1A:
  you "I swear to God you've never seen this much pink in your life!"

  "Demi laughs. Then something catches her eye on screen."

  d "I bet Cameron won't even notice."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Look at computer screen":
      jump look_at_computer_screen

label choice1B:
  you "I know I can't hide forever, but I'm in NO rush too show off my childhood bedroom."

  "Demi laughs. Then something catches her eye on screen."

  d "I bet Cameron won't even notice."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Look at computer screen":
      jump look_at_computer_screen

label look_at_computer_screen:

  "Cameron, along with all of the boys in class (and Demi) all stare intently at their screens."

  # show paoloma remove_sweatshirt
  show outline Paloma
  "Finally I notice Paloma taking off her sweatshirt revealing a paper thin tank top, and she’s clearly not wearing a bra."
  
  # show Palomao tanktop  
  you "Ugh why do I even try?"

  "Demi takes a little too long to reply."

  you "Demi?"

  "Demi tears her eyes from the screen."

  d "Oh sorry yeah. Just use a funny virtual background or something."

  $renpy.set_style_preference("choice", "default")
  menu:

    "You mean like Marcus?":
      jump choice3

    "You mean like Cameron?":
      jump choice4

label choice3:
  hide facetime demi
  show outline Marcus
  "Marcus’s background is a pixelated closeup of Professor Stein’s baldspot."

  show outline Professor
  show facetime demi
  d "Uh maybe a little classier?"

  "Suddenly a loud noise pulls my attention back to class."
  jump Jerome

label choice4:
  show outline Cameron
  "Cameron’s background is a photo of an empty casting couch."

  d "Uh maybe less bro-y?"

  "Suddenly a loud noise pulls my attention back to class."
  jump Jerome


label Jerome:
  hide facetime demi 
  show outline Anaya
  u "Woo! Take that motherfuckers!"

  "Anaya turns to yell at someone off her screen."

  a "Shut up Jerome!"

  "We all laugh."

  a "Sorry my lil bro is really into esports."

  a "And this school doesn't pay me enough to move out of my parent's place. So... deal with it."
  
  show outline Professor
  t "Ahem. Everyone open your textbooks to Kapitel 9: {i}Romantische Worte{/i}."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Open your textbook":
      $open_textbook = True
      jump choice5

    "Don't open your textbook":
      jump choice6

label choice5:
  "Even though I'm barely paying attention, I open my textbook."

  show chatbox everyone at truecenter
  "A message pops up in the Zoom chat box from 'Marcus' sent to 'Everyone'. It's a youtube link."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Click on it":
      jump choice5a

    "Don't click on it":
      jump choice5b

label choice6:
  "I don't bother, it's not like I'm paying attention anyways."

  "A message pops up in the Zoom chat box from 'Marcus' sent to 'Everyone'. It's a youtube link."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Click on it":
      jump choice5a

    "Don't click on it":
      jump choice5b

label choice5a:
  hide chatbox everyone
  show zoomwindows_blurred

  #show Anaya blurred
  #show Professor blurred
  #show Paloma blurred
  #show Cameron blurred
  #show Marcus blurred 
  #show Iman blurred 
  #show Frank blurred

  show Nein at truecenter
  "The Inglourious Basterds clip of Hitler shouting NEIN NEIN NEIN plays loudly on repeat. Thankfully my mic is muted."

  "Unfortunately Cameron's isn't. Marcus cracks up, almost falling out of his chair."

  "I can't help but laugh."
  hide Nein
  hide zoomwindows_blurred
  jump choice5c

label choice5b:
  hide chatbox everyone
  show zoomwindows_blurred
  show Nein at truecenter
  "I ignore the link but Cameron clicks on it, forgetting his mic is not muted."

  "The Inglourious Basterds clip of Hitler shouting NEIN NEIN NEIN plays loudly on repeat. Thankfully your mic is muted."
  
  "I can't help but laugh."
  hide Nein
  hide zoomwindows_blurred
  jump choice5d

label choice5c:
  show facetime demi

  "I laugh and Demi rolls her eyes so hard I can hear it in her voice."

  d "Soo mature. I can't believe you fell for it too."

  "I shrug."

  you "Aw but Cameron looks so cute when he's embarrassed."

  "An idea pops into your head."
  jump idea

label choice5d:
  show facetime demi
  "I laugh Demi rolls her eyes so hard I can hear it in her voice."

  d "Soo mature."

  you "Aw but Cameron looks so cute when he's embarrassed."

  "An idea pops into your head."
  jump idea

label idea:
  you "Oo I'll send Cameron a private message!"

  d "Okay making moves, I approve!"

  you "Ahh what do I say?"
  
  show chatbox cameron at truecenter
  
  $renpy.set_style_preference("choice", "default")
  menu:
    "Ahh what do I say?"
    
    "Compliment":
      jump choice7

    "Flirt":
      jump choice8

    "Ask Demi":
      jump choice9

label choice7:
  show chatbox cameron typing_i_like_you at truecenter
  you "Okay I'll say something nice. I like your-"

  show chatbox cameron i_like_you at truecenter
  "I type out 'I like you' and accidentally click 'send'."
  
  you "FUCK! SHIT! DAMNIT!"

  d "Woahh there."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Quickly send 'R background'":
      $fixed_message = True
      jump choice10

    "Panic":
      jump choice11

label choice8:
  you "Your good at this stuff. What's something like flirty I can say?"

  d "Stop, just tell him you like him! Cut straight to the chase."

  you "NO WAY! I'll sound like a total creep!"

  "Demi shrugs."

  d "Boys are dumb and oblivious, you've gotta cut straight to the chase. (that's why I like girls..)"

  "I roll my eyes."

  you "Okay how about"

  $renpy.set_style_preference("choice", "default")
  menu:
    "Compliment":
      jump choice7

label choice9:
  you "Come on, you've gotta help me."

  d "Ok, ok, how about will you be mein Valen-{i}stein{/i}?"

  "She cracks up at her own joke."

  you "Ha ha very funny. How about -"

  menu:

    "Flirt":
      jump choice8

    "Compliment":
      jump choice7

label choice10:
  show chatbox cameron R_background at truecenter
  "I quickly send “R background” and then leap onto my bed."
  
  hide chatbox cameron R_background
  you "I sent him ‘I like you’ instead of ‘I like your background’ I’m gonna die."

  show outline Cameron
  "Cameron’s background is an empty casting couch scene."

  show outline Professor
  d "Wait do you realize.. Nevermind."

  $renpy.set_style_preference("choice", "default")
  menu:
    "Scream into a pillow":
      jump scream_into_pillow

label choice11:
  "You leap onto your bed."

  hide chatbox cameron R_background
  you "I sent him ‘I like you’ instead of ‘I like your background’ I’m gonna die."

  show outline Cameron
  "Cameron’s background is an empty casting couch scene."
  
  show outline Professor
  d "Wait do you realize.. Nevermind."

  $renpy.set_style_preference("choice", "default")
  menu:
    "Scream into a pillow":
      jump scream_into_pillow

label scream_into_pillow:
  hide chatbox cameron R_background
  "I scream into my pillow."

  "Just then I hear a sound from Zoom."

  d "Who's that?"

  "I lift my face from my pillow."

  you "Hmm?"
  
  hide facetime demi 
  # show share screen layout

  hide mute_button
  hide text [name]
  hide outline Professor
  show bg sharescreen
  hide Professor silent
  hide Anaya silent
  hide Paloma silent
  hide Cameron silent
  hide Marcus silent
  hide Iman silent
  hide Frank silent
  show text [name]:
    xpos 1708
    xanchor 0.5
    ypos 154
    yanchor 0.5

  "Suddenly a new Zoom window takes over my laptop, entering fullscreen. Someone is 'sharing their screen'. I go back to my desk."

  you "What's going on?"
  
  # show scary video
  "On the screenshare a mouse opens up a web browser, clicks on a tab, and plays a ''GRAPHIC VIDEO''."

  "Bloody, violent footage plays of butchers carving up pigs in a slaughterhouse underscored by loud METAL music."

  "I jump back from my desk."

  you "Oh my god!"

  "A cacophony of sound as everyone unmutes their mics."

  show small_outline Frank
  f "What's happening?"

  show small_outline Cameron
  c "Shut it off!"

  show small_outline Demi
  d "Marcus stop this isn't funny."

  show small_outline Paloma
  p "Jesus Christ!"

  show small_outline Marcus
  m "I'm not the one doing this!"

  show small_outline Professor
  t "What is this Anya?"

  show small_outline Cameron
  "Cameron, a vegan, turns green and runs out of his room."

  show small_outline Iman
  "The only one calm is Iman, who is preoccupied by a steaming bowl of popcorn."
  
  # go back to zoon layer out
  scene bg zoomwithoutdemi
  hide small_outline Iman
  show mute_button mute
  show Professor silent
  show Anaya silent
  show Paloma silent
  show Cameron silent
  show Marcus silent
  show Iman silent
  show Frank silent

  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5

  "Finally the video stops."

  show outline Anaya
  a "Sorry everyone we got an anonymous “zoom bomber” or whatever. I kicked them out and turned off screen sharing. Sorry about that."

  a "(Did I mention they don't pay me enough?)"

  show outline Professor
  t "Okay calm down everyone. These trolls will not obstruct our learning."

  "He lets everyone have a moment to catch their breath."

  t "Let us read aloud from Hugo Ball’s poem on page 83. Any volunteers?"

  $renpy.set_style_preference("choice", "default")
  menu:

    "Don't Volunteer":
      jump choice12

    "Volunteer" if open_textbook:
      jump choice13

label choice12:
  "Frank's hand shoots up."
  
  show outline Professor
  t "Ahh Frank go ahead"
  
  show outline Cameron
  "Frank opens his mouth to speak, just then a loud TOILET FLUSHES from Cameron’s video as he walks back in."

  "(Yep he still hasn't figured out how to mute his mic.)"

  "Frank slightly flustered, starts to read aloud in German."
  
  show outline Frank
  f "Im dunkelblauen Sunde..."

  "Frank’s voice fades into the background."
  
  show facetime demi
  d "[name] are you okay?"

  "I'm squeezing a teddy bear to within an inch of its life."

  $renpy.set_style_preference("choice", "default")
  menu:

    "No, I'm not":
      jump choice14

    "Yeah ...":
      jump choice15

label choice13:
  "Since my textbook is open I consider volunteering..."

  "But I'm too shaken up from what just happened."
  
  show outline Frank
  "Thankfully Frank raises his hand. His voice fades into the background as he reads aloud in German."

  show facetime demi
  d "[name] are you okay?"

  "I'm squeezing a teddy bear to within an inch of its life."

  $renpy.set_style_preference("choice", "default")
  menu:

    "No, I'm not":
      jump choice14

    "Yeah ...":
      jump choice15

label choice14:
  you "No, not really"

  d "Yeah, that was.. weird."

  "We're both silent for a moment."

  d "Did Cameron message you back?"

  "Oh yeah, I completely forgot!"

  $renpy.set_style_preference("choice", "default")
  menu:

    "Open your chat box":
      jump choice16

label choice15:
  you "Yeah, that was.. weird."

  d "Yeah."

  "We're both silent for a moment."

  d "Did Cameron message you back?"

  "Oh yeah, I completely forgot!"

  $renpy.set_style_preference("choice", "default")
  menu:

    "Open your chat box":
      jump choice16

label choice16:
  # show cameron chatbox
  you "Wait he did!"

  "My mood instantly changes."

  d "Awesome, what’d he say?"

  if fixed_message:
    jump choice17

  else:
    jump choice18      

label choice17:
  show chatbox cameron haha_thanks at truecenter
  "I read Cameron's message aloud."

  you "He said 'Haha Thanks'. Isn't he so sweet?"

  "Demi rolls her eyes."

  d "Someone's clearly smitten..."

  "I start to type a reply, but something catches my attention."
  hide chatbox cameron haha_thanks
  jump background_changed

label choice18:
  show chatbox cameron uh_thanks at truecenter
  "I read Cameron's message aloud"

  you "He just said, 'Uh thanks I guess?'"

  "Blood drains from my face, as I realize-"

  you "I NEVER FIXED MY MESSAGE! I just sent him 'I like you'!"

  d "Uh oh.."

  you "Oh God how do I fix this??"
  
  hide chatbox cameron uh_thanks
  "I start to type a reply, but something catches my attention."

  jump background_changed

label background_changed:
  #show masked figure

  #masked figure sits on couch with face turned away
  "Now sitting on the couch in Cameron's virtual background is a FIGURE wearing a hoodie, their face obscured."

  you "Wait his background changed."

  d "I guess?"

  you "Maybe I should ask him where he got it."

   #masked figure turns face
  "The figure on the couch slowly turns towards the camera,"

  #masked figure shows face
  " revealing a creepy MASK."

  you "What the -"
  
  #figure stands
  "Unnoticed by Cameron the Masked Figure gets up from the couch"

  #figure stands closer with knife
  "and creeps up behind him, pulling out a large butcher KNIFE."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Warn Him!":
      jump Warn_Him

    "SCREAM!":
      jump SCREAM

label Warn_Him:
   you "Cameron LOOK OUT!"

   #figure gets even closer
   "I try to warn him but my {b}mic is muted!{/b} He can't hear me."
   
   scene bg zoomwithoutcameron
   show Cameron glitch
   show mute_button mute
   show Professor silent
   show Anaya silent
   show Paloma silent
   show Marcus silent
   show Iman silent
   show Frank silent
   show facetime demi

   show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5

   "Cameron’s webcam GLITCHES "
   
   scene bg zoomwindows
   show mute_button mute
   show Professor silent
   show Anaya silent
   show Paloma silent
   show Cameron silent
   show Marcus silent
   show Iman silent
   show Frank silent
   show facetime demi

   show text [name]:
     xpos 358
     xanchor 0.5
     ypos 258
     yanchor 0.5
   
   scene bg zoomwithoutcameron
   show mute_button mute
   show Professor silent
   show Anaya silent
   show Paloma silent
   show Marcus silent
   show Iman silent
   show Frank silent
   show facetime demi
   " and cuts to black. "

   #8 windows exists instead of 9
   scene bg zoom8windows
   show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5

   show Professor silent
   show Anaya silent
   show Paloma silent
   show Marcus silent8
   #show Demi silent8
   show Iman silent8
   show Frank silent8
   show facetime demi
   
   " Then Cameron’s screen logs out of Zoom altogether."

   d "What's going on? Are you ok?"

   jump Oh_my_God

label SCREAM:
  "I scream at the top of your lungs, but my {b}mic is muted!{/b} He can't hear me."

  scene bg zoomwithoutcameron
  show mute_button mute
  show Professor silent
  show Anaya silent
  show Paloma silent
  show Marcus silent
  show Iman silent
  show Frank silent
  show facetime demi

  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5
  show Cameron glitch

  "Cameron’s webcam GLITCHES "

  scene bg zoomwindows
  show mute_button mute
  show Professor silent
  show Anaya silent
  show Paloma silent
  show Cameron silent
  show Marcus silent
  show Iman silent
  show Frank silent
  show facetime demi

  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5
   
  scene bg zoomwithoutcameron
  show facetime demi
  " and cuts to black. "

  #8 windows exists instead of 9
  scene bg zoom8windows
  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5

  show Professor silent
  show Anaya silent
  show Paloma silent
  show Marcus silent8
  show Demi silent8
  show Iman silent8
  show Frank silent8
  show facetime demi 

  "Then Cameron’s screen logs out of Zoom altogether."

  d "Why are you screaming?!"

  jump Oh_my_God

label Oh_my_God:
  you "Oh my god did you see that?"

  d "see what?"

  you "Cameron! He just got attacked!"

  d "What’re you talking about his laptop probably died."

  you "No I’m telling you I saw someone move on his screen."

  d "Are you sure it wasn’t just his background?"

  "The Masked Figure reappears, now in the back of Iman’s screen."

  you "Look it's on Iman's now!"

  $renpy.set_style_preference("choice", "default")
  menu:

    "Turn on mic":
      jump Turn_on_mic

    "Turn on video":
      jump Turn_on_video_1

    "Send a chat message":
      jump Send_chat_message

    "Take a screenshot":
      $screenshot_iman = True
      jump Take_screenshot 

#mix mic
label Turn_on_mic:

  show mute_button unmute
  "I turn on my mic."

  you "I-man ... Run!"

  "But my audio is still full of static, Iman can't hear me."

  you "Damnit!"
  
  show mute_button mute
  "I mute my mic."

  jump Send_chat_message

label Turn_on_video_1:
  hide facetime demi
  show mute_button unmute
  "I turn on my video for the first time all class and unmute."

  show outline player
  you "Did anyone .. see ... mask?"

  "my audio cuts in and out."
  
  show outline Anaya
  a "[name]? What are you talking about?"

  show outline player
  you "In ... the ... videos! He .. has a knife!"

  "My voice trails off..."

  "I just noticed "

  "the figure behind me, {b}on my screen!{/b}"

  you "Like that."

  scene bg zoom

  jump Bad_Ending

label Send_chat_message:
  # show chatbox Iman
  "I frantically send Iman a private message."
  
  show chatbox iman at truecenter
  you "TURN AROUND!"

  hide chatbox iman
  "But I'm too late."

  "The Masked Figure comes up behind her brandishing the same knife."

  #show Iman glitch
  "Her screen cuts to STATIC"

  #show 7 windows
  scene bg zoom7windows
  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5
  show Professor silent
  show Anaya silent
  show Paloma silent
  show Marcus silent
  show Frank silent7
  show facetime demi
  "and then she to logs out."

  you "No!"

  d "Okay that's kinda weird. Maybe something is wrong with the internet connection?"

  d "Let me try popping back into the Zoom."

  you "Uh... Okay..?"

  # remove demi
  hide facetime demi
  scene bg zoom7demiblack
  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5
  show Professor silent
  show Anaya silent
  show Paloma silent
  show Marcus silent
  show Frank silent7

  "Demi's square dissappears briefly."

  # bring back demi on
  scene bg zoom7demi
  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 258
    yanchor 0.5
  show Demi silent7
  show Professor silent
  show Anaya silent
  show Paloma silent
  show Marcus silent
  show Frank silent7
  show facetime demi
  "When she reenters the Zoom, her video is on."

  d "See nothing- Oops forgot everyone can see me."

  "The figure reappears a 3rd time, now in ''Demi’s background''!"

  if screenshot_iman:
    $renpy.set_style_preference("choice", "default")
    menu:

      "Tell her to turn around":
        jump Turn_around

      "Turn on video":
        jump Turn_on_video_1

  else:
    $renpy.set_style_preference("choice", "default")
    menu:

      "Tell her to turn around":
        jump Turn_around

      "Turn on video":
        jump Turn_on_video_1

      "Take a screen shot":
        $screenshot_demi = True
        jump option2

label Take_screenshot:
  # animate flash
  # screenshot sound
  define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

  show bg zoom8windows with flashbulb
 
  "I quickly take a screenshot of Iman's screen. The Masked Figure still looms behind her in the background."
  
  $renpy.set_style_preference("choice", "default")
  menu:

    "Turn on mic":
      jump Turn_on_mic

    "Turn on video":
      jump Turn_on_video_1

    "Send a chat message":
      jump Send_chat_message

label option2:
  define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

  show bg zoom7demi with flashbulb

  "I quickly take a screenshot of Demi's screen. The Masked Figure still looms behind her in the background."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Tell her to turn around":
      jump Turn_around

    "Turn on video":
      jump Turn_on_video_1

label Turn_around:
  you "DEMI He's right behind you! Turn around!"

  d "What?"

  "Demi glances behind her."

  d "Calm down there's no one here."

  you "But I can see him."

  #show glitch and facetime fades to black screen
  show facetime fade
  "Demi’s screen glitches and suddenly the figure appears right over Demi’s shoulder. The mask fills the screen."

  # show 6 windows
  scene bg zoom6windows
  show text [name]:
    xpos 358
    xanchor 0.5
    ypos 410
    yanchor 0.5
  show Professor silent6
  show Anaya silent6
  show Paloma silent6
  show Marcus silent6
  show Frank silent6 

  "I SCREAM, just as Demi’s video logs out and she hangs up the phone."

  you "Demi? Demi! Are you okay? Where are you?"

  $renpy.set_style_preference("choice", "default")
  menu:

    "Call her back":
      jump Call_her_back

    "Turn on video":
      jump Turn_on_video_2

    "Turn on mic":
      jump option3

label Call_her_back:
  $choice_in_textbox = True
 
  #show facetime calling
  show facetime demi
  "I pick up my phone and try to call her back, but there's nothing but a dial tone on the other end."

  ""

  hide facetime demi
  ""

  $renpy.set_style_preference("choice", "hidden_choice")
  menu:
    t " " 

    "Turn on your video":
      jump Turn_on_video5

    "Class is not over! You must stay on Zoom.":
      jump option4

label option3:
  "I take a deep breath and try to calm down. There must be some explanation for this."

  show mute_button unmute6
  "I turn on my mic."

  you "Um did  ..zzz ... ZZzzz"

  "My audio is full of static."

  show outline Professor6
  t "Excuse me? Who is that? I can't hear you."

  "Sigh, this isn't working."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Turn on video":
      jump Turn_on_video_2

label Turn_on_video_2:
  hide facetime demi
  show mute_button unmute6
  "I turn on my video for the first time all class and unmute."

  show outline player6
  you "Did anyone .. see ... mask?"

  "my audio cuts in and out."
  
  show outline Anaya6
  a "[name]? What are you talking about?"

  show outline player6
  you "In ... the ... videos! He .. has a knife!"

  "My voice trails off..."

  "I just noticed "

  "the figure behind me, {b}on my screen!{/b}"

  you "Like that."

  scene bg zoom

  jump Bad_Ending

label option4:
  # animationof windows leaving 
  "I watch in horror as the masked figure pops up in everyone's video one-by-one. The same sequence of events happens in each video. The knife, then a glitch, and then black."
  
  #3 boxes left
  scene bg zoom3windows

  "The boxes drop off like dominoes until its only me, Anaya, and Paloma left, even the Professor is gone."

  show outline Paloma3
  p "Hello? Guys?"

  show outline Anaya3 
  a "This isn't funny."
  
  $renpy.set_style_preference("choice", "default")
  menu:

    "Turn on video":
      jump Turn_on_video_6

    "Turn on mic":
      jump option5

label option5:
  show mute_button unmute3
  show outline player3
  you "Did anyone else see the man in the mask?"

  "Finally, miraculously my audio comes through clearly."

  show outline Anaya3
  a "[name]? What are you talking about?"

  show outline player3
  you "In the background of everyone's videos! He attacked them! He has a knife!"

  show outline Paloma3
  p "I-I didn't see anyone.."

  show outline Anaya3
  a "Is this some kind of joke? Now that you've finally decided to join class -"
  
  show outline player3
  you "I'm serious!"
  
  $renpy.set_style_preference("choice", "default")
  menu:

    "Turn on your video":
      jump Bad_Ending_2

    "Share screen" if screenshot_iman:
      jump Share_your_screen

    "Share screen" if screenshot_demi:
      jump Share_your_screen

label Turn_on_video5:
  show mute_button unmute6
  "I turn on my video for the first time all class and unmute."

  show outline player6
  you "Did anyone .. see ... mask?"

  "my audio cuts in and out."
  
  show outline Anaya6
  a "[name]? What are you talking about?"

  show outline player6
  you "In ... the ... videos! He .. has a knife!"

  "My voice trails off..."

  "I just noticed "

  "the figure behind me, {b}on my screen!{/b}"

  you "Like that."

  scene bg zoom

  jump Bad_Ending

label Turn_on_video_6:
  show mute_button unmute3
  "I turn on my video for the first time all class and unmute."

  show outline player3
  you "Did anyone .. see ... mask?"

  "my audio cuts in and out."
  
  show outline Anaya3
  a "[name]? What are you talking about?"

  show outline player3
  you "In ... the ... videos! He .. has a knife!"

  "My voice trails off..."

  "I just noticed "

  "the figure behind me, {b}on my screen!{/b}"

  you "Like that."

  scene bg zoom

  jump Bad_Ending

label Share_your_screen:
  show outline player3
  you "I have proof!"

  #if screenshot_iman show Iman_screenshot
  #if screenshot_demi show Demi_screenshot
  "I pull up the screenshot I took earlier and share my screen."

  show outline Paloma3
  p "Um okay, why are we looking at a picture of class?"

  show outline Anaya3
  a "There's no recording of the class allowed! I could write you up for this."

  if screenshot_iman:
    show outline player3
    you "Whatever. Don't you see the guy behind Iman?"

  if screenshot_demi:
    show outline player3
    you "Whatever. Don't you see the guy behind Demi?"

  show outline Paloma3
  p "Nothing's there [name]. I knew you were weird, but not like {i}that{/i} weird.."

  show outline player3
  you "What he's right - "

  show outline Anaya3
  "Anaya cuts you off."

  show outline Anaya3
  a "I think I'll end class early, there must be some connection issue."

  a "and [name], we'll talk about this screenshotting business later..." 

  a "Look out for an email from me tomorrow okay?"

  show outline player3
  you "But-"

  show outline Anaya3
  a "Class is over."

  $renpy.set_style_preference("choice", "default")
  menu:

    "Logout":
      jump Good_ending

label Bad_Ending:

  "The Masked Figure is in my room, {b}he's real{/b}."

  "There's nowhere to run, nowhere to hide."

  "The last thing I see is the flash of his knife before I- "

  "{b}Bad Ending{/b}."

  jump Credits

label Bad_Ending_2:
  show mute_button unmute3
  "I turn on my video for the first time all class and unmute."

  show outline player6
  you "Did anyone .. see ... mask?"

  "my audio cuts in and out."
  
  show outline Anaya6
  a "[name]? What are you talking about?"

  show outline player6
  you "In ... the ... videos! He .. has a knife!"

  "My voice trails off..."

  "I just noticed "

  "the figure behind me, {b}on my screen!{/b}"

  you "Like that."

  hide playerwindowview6
  hide Professor background6
  hide anaya background6
  hide Paloma background6
  hide Marcus background6
  hide Frank background6
  hide outline player6
  hide mute_button mute6
  hide text [name]
  show playerwindow

  jump Bad_Ending
  jump Bad_Ending

label Good_ending:
   
  "I consider trying to plead my case but clearly these two are never going to believe me."

  "Plus I might be in trouble?"
  scene bg player_desktop 
  "I move my cursor to log out but then Anaya ends the class, booting us out of the Zoom."

  "Well that was weird. I look at the clock on my desk, it's pretty late." 

  "Maybe Anaya is right and I was just imagining things." 

  "Maybe everyone just ran out of battery, or their Wifi signal dropped."

  "Demi's phone probably died, that happens all the time."

  "Yeah, I'll call Demi first thing in the morning, after she's recharged her phone." 

  "I climb into bed and drift off to sleep."

  "Safe and sound."

  #start new sceen, no more zoom window, it's Anaya's computer showing her view from her webcam

  scene bg jerome_background
  show Anaya silent2
  show Jerome silent
  "Anaya ends the Zoom meeting, pulls out her earbuds and laughs maniacally."

  "She turns to her younger brother JEROME, sitting at a souped up PC station next to her."

  a "Nice Zoom-bombing. The music in that video was a great touch."

  j "Thanks. Can you log on now? Our team needs you."

  a "Sure, I've got lots of free time now."

  "ANAYA leans back in her chair and puts on a gaming headset."

  "She pauses."

  a "By the way, where did you get the mask?"

  j "Huh?"

  a "The mask in everyone's background. The knife was a good touch too, super creepy."

  j "What are you talking about? What knife? Can we just play?"

  "A look of horror slowly dawns on Anaya's face."

  "Her computer screen ''GLITCHES''..."

  "{b}Good Ending{/b}."

  jump Credits

label Credits:
  "Thanks for playing Zoombomber!"

  "Written by: Jumai Yusuf"

  "Illustrations by: Toyin Yusuf"

  "Coding and Zoom layout by: Tobi Yusuf"


return
