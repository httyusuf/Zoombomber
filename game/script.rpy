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

# your character
define you = Character('[name]', color="#0080c0")

play music "02 Like a Refreshing Sunrise.mp3"

show playerwindow

show text "[name]" at truecenter

"I am in an online class named German 101 held on Zoom."

hide playerwindow
hide text

show playerwindowview

show text "[name]":
    xpos 238
    xanchor 0.5
    ypos 172
    yanchor 0.5

show outline professor
show professor background
show anaya background
show Frank background
show Cameron background
show Marcus background
show Demi background
show Iman background
show Paloma background

"The white-haired Professor ALFRED STEIN (60s) sits in the upper middle corner. Followed by the students, all in their early 20s:"

show outline Anaya
"ANAYA (26) - the bored teacher’s assistant,"

show outline Paloma
"PALOMA - the hot Latin American foreign exchange student,"

show outline Cameron
"CAMERON - the cool, surfer, heartthrob,"

show outline Marcus
"MARCUS - the class clown,"

show outline Demi
"DEMI - the tomboyish athlete,"

show outline Iman
"IMAN - South Asian, the heavy snacker,"

show outline Frank
"and FRANK - the Aryan A+ student."

show mute_button mute
"I turn off my video and and mute my mic."

hide mute_button mute

$renpy.set_style_preference("choice", "default")
menu:
    "Press start."

    "Start":
      jump start_class

label start_class:
  show outline professor
  t "Do we have everyone Anya?"

  show outline Anaya
  a "It's Anaya. A-NA-YA"

  show outline professor
  t "Right. Why can’t I see someone’s video? Who is that {color=#0080c0}[name]{/color}?"

  show mute_button unmute
  "You unmute your mic."

  hide mute_button unmute

  show outline player
  you "Yes ... s-sorry ... my ... camera ... working ... some reason."

  show outline Anaya
  a "Sounds like [name] is having wifi issues."

  show outline professor
  t "Fine, fine. In honor of {i}Valentinstag{/i} approaching, today we will be exploring some beautiful German poetry..."

  "Professor Stein drones on and on."
  
  # show incoming call photo in top right corner
  show phone_call demi
  "You mute your mic and let out a sigh of relief. Suddenly your cell phone ''rings''."

  menu:
   "Pick up the phone."

   "You pick it up":
     jump scene_2

label scene_2:
  hide phone_call demi

  #show facetime
  show facetime demi
  "You pick up your phone, it's ''DEMI'' your best friend who is also in the class."

  d "Hey girl!"

  menu:
    "what do you say?"

    "Do you think he bought it?":
      jump choice1

    "Was that convincing enough?":
      jump choice2

label choice1:
  d "He barely knows how to use a laptop I’m sure you’re fine."

  you "Ok good because I can NOT let Cameron see my room. I’ll never live this down."

  d "Come on are you going to hide for the rest of the semester? It can’t be that bad."

  menu:
    "what do you say?"

    "No it's even worse than you think":
      jump choice1A

    "Yeah I guess you're right..":
      jump choice1B

label choice2:
  d "Yeah you can {i}totally{/i} leave your camera and mic off for the rest of class."

  you "Ok good because I can NOT let Cameron see my room. I’ll never live this down."

  d "Come on are you going to hide for the rest of the semester? It can’t be that bad."

  menu:
    "what do you say?"

    "No it's even worse than you think":
      jump choice1A

    "Yeah I guess you're right..":
      jump choice1B

label choice1A:
  you "I swear to God you've never seen this much pink in your life!"

  "Demi laughs. Then something catches her eye on screen."

  d "I bet Cameron won't even notice."

  menu:
    "What do you do?"

    "Look at computer screen":
      jump look_at_computer_screen

label choice1B:
  you "I know I can't hide forever, but I'm in NO rush too show off my childhood bedroom."

  "Demi laughs. Then something catches her eye on screen."

  d "I bet Cameron won't even notice."

  menu:
    "What do you do?"

    "Look at computer screen":
      jump look_at_computer_screen

label look_at_computer_screen:
  "Cameron, along with all of the boys in class (and Demi) all stare intently at their screens."

  # show paoloma remove_sweatshirt
  "Finally you notice Paloma has taken off her sweatshirt revealing a paper thin tank top, and she’s clearly not wearing a bra."
  
  # show palomao tanktop  
  you "Ugh why do I even try?"

  "Demi takes a little too long to reply."

  "Demi?"

  "Demi tears her eyes from the screen."

  d "Oh sorry yeah. Just use a funny virtual background or something."

  menu:
    "What do you do?"

    "You mean like Marcus?":
      jump choice3

    "You mean like Cameron?":
      jump choice4

label choice3:
  "Marcus’s background is a pixelated closeup of Professor Stein’s baldspot."

  d "Uh maybe a little classier?"

  "Suddenly a loud noise pulls your attention back to class."
  jump Jerome

label choice4:
  "Cameron’s background is a photo of an empty casting couch."

  d "Uh maybe less bro-y?"

  "Suddenly a loud noise pulls your attention back to class."
  jump Jerome

label Jerome:
  show outline Anaya
  u "Woo! Take that motherfuckers!"

  "Anaya turns to yell at someone off her screen."

  a "Shut up Jerome!"

  "You all laugh."

  a "Sorry my lil bro is really into esports."
  
  show outline professor
  t "Ahem. Everyone open your textbooks to Kapitel 9: {i}Romantische Worte{/i}."

  menu:
    "What do you do?"

    "Open your textbook":
      $open_textbook = True
      jump choice5

    "Don't open your textbook":
      jump choice6

label choice5:
  "Even though you're barely paying attention, you open your textbook."

  show chatbox everyone at truecenter
  "A message pops up in the Zoom chat box from 'Marcus' sent to 'Everyone'. It's a youtube link."

  menu:
    "What do you do?"

    "Click on it":
      jump choice5a

    "Don't click on it":
      jump choice5b

label choice6:
  "You don't bother, its not like you're paying attention anyways."

  "A message pops up in the Zoom chat box from 'Marcus' sent to 'Everyone'. It's a youtube link."

  menu:
    "What do you do?"

    "Click on it":
      jump choice5a

    "Don't click on it":
      jump choice5b

label choice5a:
  hide chatbox everyone
  # show Hitler Video
  "The Inglourious Basterds clip of Hitler shouting NEIN NEIN NEIN plays loudly on repeat. Thankfully your mic is muted."

  "Unfortunately Cameron's isn't. Marcus cracks up, almost falling out of his chair."

  "You can't help but laugh"
  jump choice5c

label choice5b:
  hide chatbox everyone
  "You ignore the link but Cameron clicks on it, forgetting his mic is not muted."

  "The Inglourious Basterds clip of Hitler shouting NEIN NEIN NEIN plays loudly on repeat. Thankfully your mic is muted."
  
  "You can't help but laugh"
  # hide Htiler video
  jump choice5d

label choice5c:
  "Demi rolls her eyes so hard you can hear it in her voice."

  d "Soo mature. I can't believe you fell for it too."

  "you shrug."

  you "Aw but Cameron looks so cute when he's embarrassed."

  "An idea pops into your head."
  jump idea

label choice5d:
  "Demi rolls her eyes so hard you can hear it in her voice."

  d "Soo mature."

  you "Aw but Cameron looks so cute when he's embarrassed."

  "An idea pops into your head."
  jump idea

label idea:
  you "Oo I'll send Cameron a private message!"

  d "Okay making moves, I approve!"

  you "Ahh what do I say?"
  
  show chatbox cameron at truecenter
  
  menu:
    "What do you do?"

    "I like your background":
      jump choice7

    "I like you":
      jump choice8

    "Will you be mein Valen-stein?":
      jump choice9

label choice7:
  you "Okay I like your-"

  #show typing I like you
  "You type out 'I like you' and accidentally click 'send'."
  
  #show I like you
  you "FUCK! SHIT! DAMNIT!"

  d "Woahh there."

  menu:
    "What do you do?"

    "Quickly send 'R background'":
      $fixed_message = True
      jump choice10

    "Panic":
      jump choice11

label choice8:
  d "Just tell him you like him! Cut straight to the chase."

  you "NO WAY! Are you trying to make me sound like a creep?"

  "Demi shrungs."

  d "Boys are dumb and oblivious, you've gotta cut straight to the chase. (that's why I like girls..)"

  "You roll your eyes."

  you "Okay how about"

  menu:
    "I like your background":
      jump choice7

label choice9:
  d "How about will you be mein Valen-{i}stein{/i}?"

  "She cracks up at her own joke."

  you "Ha ha very funny. How about -"

  menu:
    "What do you do?"

    "I like you":
      jump choice8

    "I like your background":
      jump choice7

label choice10:
  # show R_background
  "You quickly sends “R background” and then leap onto your bed."

  you "I sent him ‘I like you’ instead of ‘I like your background’ I’m gonna die."

  "Cameron’s background is an empty casting couch scene."

  d "Wait do you realize.. Nevermind."

  "You screem into a pillow"

  jump scream_into_pillow

label choice11:
  "You leap onto your bed."

  you "I sent him ‘I like you’ instead of ‘I like your background’ I’m gonna die."

  "Cameron’s background is an empty casting couch scene."

  d "Wait do you realize.. Nevermind."

  "You screem into a pillow"

  jump scream_into_pillow

label scream_into_pillow:
  hide chatbox cameron
  "Meanwhile a ''new window'' pops up on the screen. The video is turned off"

  d "Who's that?"

  "You lift your face from your pillow."

  you "Hmm?"
  
  # show share_screen
  "Suddenly the Zoom window takes over your laptop, entering fullscreen. Someone is 'sharing their screen'. You go back to your desk."

  you "What's going on?"
  
  # show scary video
  "On the screenshare a mouse opens up a web browser, clicks on a tab, and plays a ''GRAPHIC VIDEO''."

  "Bloody, violent footage plays of butchers carving up pigs in a slaughterhouse underscored by loud METAL music."

  "You jump back from your desk."

  you "Oh my god!"

  "A cacophony of sound as everyone unmutes their mics."

  show outline Frank
  f "What's happening?"

  show outline Cameron
  c "Shut it off!"

  show outline Demi
  d "Marcus stop this isn't funny."

  show outline Paloma
  p "Jesus Christ!"

  show outline Marcus
  m "I'm not the one doing this!"

  show outline professor
  t "What is this Anya?"

  "Cameron, a vegan, turns green and runs out of his room."

  "The only one calm is Iman, who is preoccupied by a steaming bowl of popcorn."
  
  # go back to zoon layer out
  "Finally the video stops."

  show outline Anaya
  a "Sorry everyone we got an anonymous “zoom bomber” or whatever. I kicked them out and turned off screen sharing. Sorry about that."

  show outline professor
  t "Okay calm down everyone. These trolls will not obstruct our learning."

  "He lets everyone have a moment to catch their breath."

  t "Let us read aloud from Hugo Ball’s poem on page 83. Any volunteers?"

  menu:
    "What do you do?"

    "Don't Volunteer":
      jump choice12

    "Volunteer" if open_textbook:
      jump choice13

label choice12:
  "Frank's hand shoots up."
  
  show outline professor
  t "Ahh Frank go ahead"
  
  show outline Cameron
  "Frank opens his mouth to speak, just then a loud TOILET FLUSHES from Cameron’s video as he walks back in."

  "(Yep he still hasn't figured out how to mute his mic.)"

  "Frank slightly flustered, starts to read aloud in German."
  
  show outline Frank
  f "Im dunkelblauen Sunde..."

  "Frank’s voice fades into the background."

  d "[name] are you okay?"

  "You're squeezing a teddy bear to within an inch of its life."

  menu:
    "What do you do?"

    "No, I'm not":
      jump choice14

    "Yeah ...":
      jump choice15

label choice13:
  "Since you're textbook is open you consider volunteering..."

  "But you're too shaken up from what just happened."
  
  show outline Frank
  "Thankfully Frank raises his hand. His voice fades into the background as he reads aloud in German."

  d "[name] are you okay?"

  "You're squeezing a teddy bear to within an inch of its life."

  menu:
    "What do you do?"

    "No, I'm not":
      jump choice14

    "Yeah ...":
      jump choice15

label choice14:
  you "No, not really"

  d "Yeah, that was.. weird."

  "both of you are silent for a moment."

  d "Did Cameron message you back?"

  "Oh yeah, you completely forgot!"

  menu:
    "What do you do?"

    "Open your chat box":
      jump choice16

label choice15:
  you "Yeah, that was.. weird."

  d "Yeah."

  "both of you are silent for a moment."

  d "Did Cameron message you back?"

  "Oh yeah, you completely forgot!"

  menu:
    "What do you do?"

    "Open your chat box":
      jump choice16

label choice16:
  # show cameron chatbox
  you "Wait he did!"

  "Your mood instantly changes."

  d "Awesome, what’d he say?"

  if fixed_message:
    jump choice17

  else:
    jump choice18      

label choice17:
  "You read Cameron's message."

  you "He said 'Haha Thanks'. Isn't he so sweet?"

  "Demi rolls her eyes."

  d "Someone's clearly smitten..."

  "You start to type a reply, but something catches your attention."

  jump background_changed

label choice18:
  "You read Cameron's message."

  you "He just said, 'Uh thanks I guess?'"

  "Blood drains from your face, as you realize-"

  you "I NEVER FIXED MY MESSAGE! I just sent him 'I like you'!"

  d "Uh oh.."

  you "Oh God how do I fix this??"

  "You start to type a reply, but something catches your attention."

  jump background_changed

label background_changed:
  "Now sitting on the couch in Cameron's virtual background is a FIGURE wearing a hoodie, their face obscured."

  d "I guess?"

  you "Maybe I should ask him where he got it."

  "The figure on the couch slowly turns towards the camera, revealing a creepy MASK."

  you "What the -"
  
  #show masked figure
  "Unnoticed by Cameron the Masked Figure gets up from the couch and creeps up behind him, pulling out a large butcher KNIFE."

  menu:
    "What do you do?"

    "Warn Him!":
      jump Warn_Him

    "SCREAM!":
      jump SCREAM

label Warn_Him:
   you "Cameron LOOK OUT!"

   "You try to warn him but your {b}mic is muted!{/b} He can't hear you."
   
   # show background glitch
   "Cameron’s webcam GLITCHES and cuts to black. Then Cameron’s screen logs out of Zoom altogether."

   d "What's going on? Are you ok?"

   jump Oh_my_God

label SCREAM:
  "You scream at the top of your lungs, but your ''mic is muted''. He can't hear you."

  "Cameron’s webcam GLITCHES and cuts to black. Then Cameron’s screen logs out of Zoom altogether."

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

  menu:
    "What do you do?"

    "Turn on your mic":
      jump Turn_on_mic

    "Turn on your video":
      jump Turn_on_video

    "Send a chat message":
      jump Send_chat_message

    "Take a screenshot":
      $screenshot_iman = True
      jump Take_screenshot

label Turn_on_mic:
  "You turn on your mic."

  you "I-man ... Run!"

  "But your audio is full of static, Iman can't hear you."

  you "Damnit!"

  "You mute your mic."

  jump Send_chat_message

label Turn_on_video:
  "You turn on your video for the first time all class."

  you "Did anyone .. see ... mask?"
  
  show outline Anaya
  a "[name]? What are you talking about?"

  you "In ... the ... videos! He .. has a knife!"

  "Your voice trails off."

  "You just noticed the figure behind you, ''on your own screen!''"

  you "Like that."

  jump Bad_Ending

label Send_chat_message:
  # shoe chatbox Iman
  "You frantically send Iman a private message."

  you "TURN AROUND!"

  "But you're too late."

  "The Masked Figure comes up behind her brandishing the same knife. Her screen cuts to STATIC and then she too logs out."

  "No!"

  d "Okay that’s kinda weird. Maybe the internet connection is wonky or-?"

  "The figure reappears a 3rd time, now in ''Demi’s background''!"

  if screenshot_iman:
    menu: 
      "What do you do?"

      "Tell her to turn around":
        jump Turn_around

      "Turn_on_video":
        jump Turn_on_video

  else:
    menu:
      "What do you do?"

      "Tell her to turn around":
        jump Turn_around

      "Turn_on_video":
        jump Turn_on_video

      "Take a screen shot":
        $screenshot_demi = True
        jump option2

label Take_screenshot:
  "You quickly take a screenshot of Iman's screen. The Masked Figure still looms behind her in the background."
  
  menu:
    "What do you do?"

    "Turn on your mic":
      jump Turn_on_mic

    "Turn on your video":
      jump Turn_on_video

    "Send a chat message":
      jump Send_chat_message

label option2:
  "You quickly take a screenshot of Demi's screen. The Masked Figure still looms behind her in the background."

  menu:
    "What do you do?"

    "Tell her to turn around":
      jump Turn_around

    "Turn on your video":
      jump Turn_on_video

label Turn_around:
  you "DEMI He's right behind you! Turn around!"

  d "What?"

  "Demi glances behind her."

  d "Calm down there's no one here."

  you "But I can see him"

  "Demi’s screen glitches and suddenly the figure appears right over Demi’s shoulder. The mask fills the screen."

  "You SCREAM, just as Demi’s video logs out and she hangs up the phone."

  you "Demi? Demi! Are you okay? Where are you?"

  menu:
    "What do you do?"

    "Call her back":

      jump Call_her_back

    "Turn on your video":
      jump Turn_on_video

    "Turn on you mic":
      jump option3

label Call_her_back:
  $choice_in_textbox = True

  "You pick up your phone and try to call her back, but there's nothing but a dial tone on the other end."

  t "Hey why are people leaving. Class is not over!"
  
  $renpy.set_style_preference("choice", "hidden_choice")
  menu:
    " " 

    "Turn on your video":
      jump Turn_on_video

    "Class is not over!":
      jump option4

label option3:
  "You take a deep breath and try to calm down. There must be some explanation for this."

  "You turn on your mic."

  you "Um did  ..zzz ... ZZzzz"

  "Your audio is full of static."

  t "Excuse me? Who is that? I can't hear you."

  "You sigh, this isn't working."

  menu:
    "What do you do?"

    "Turn on your video":
      jump Turn_on_video

label option4:
  "You watch in horror as the masked figure pops up in everyone's video one-by-one."

  "The same sequence of events happens in each video. The knife, then a glitch, and then black."

  "The boxes drop off like dominoes until its only you, Anaya, and Marcus left."

  m "Hello? Guys?"

  a "This isn't funny."
  
  $renpy.set_style_preference("choice", "default")
  menu:
    "What do you do?"

    "Turn on your video":
      jump Turn_on_video

    "Turn on your mic":
      jump option5

label option5:
  you "Did anyone else see the man in the mask?"

  "Finally your audio comes through clearly."

  a "[name]? What are you talking about?"

  you "In the background of everyone's videos! He attacked them! He has a knife!"

  m "I-I didn't see anyone.."

  a "Is this some kind of joke? Now that you've finally decided to join class -"

  you "I'm serious!"
  
  menu:
    "What do you do?"

    "Turn on your video":
      jump Bad_Ending_2

    "Share your screen" if screenshot_iman:
      jump Share_your_screen

    "Share your screen" if screenshot_demi:
      jump Share_your_screen

label Share_your_screen:
  you "I have proof!"

  "You pull up the screenshot you took earlier and share your screen."

  m "Um okay, why are we looking at a picture of class?"

  if screenshot_iman:
    you "Don't you see the guy behind Iman?"

  if screenshot_demi:
    you "Don't you see the guy behind Demi?"

  a "Nothing's there [name]."

  you "What he's right - "

  "Anaya cuts you off."

  a "I think I'll end class early, there must be some connection issue. Look out for an email from me tomorrow okay?"

  you "But-"

  a "Class is over."

  menu:
    "What do you do?"

    "Logout":
      jump Good_ending

label Bad_Ending:
  "The Masked Figure is in your room, {b}he's real{/b}."

  "There's nowhere to run, nowehere to hide."

  "The last thing you see is the flash of his knife before you die."

  "{b}Bad Ending{/b}."

  jump Credits

label Bad_Ending_2:
  "You turn on your video for the first time all class."

  you "I really saw someone I swear! He showed up right before they logged off. I don't know if its a virus or something but the guy looked pretty scary..."

  "Your voice trails off."

  "You just noticed the figure behind you, ''on your own screen!''"

  you "... Like that."

  "You turn around."

  jump Bad_Ending

label Good_ending:
  "Anaya ends the meeting, she pulls out her earbuds and laughs."

  "She turns to her younger brother JEROME, sitting at a souped up PC station next to her."

  a "Nice hacking. The music was a great touch."

  j "Thanks. Can you log on now? Our team needs you."

  a "Sure, I've got lots of free time now."

  "ANAYA leans back in her chair and puts on a gaming headset."

  "She pauses."

  a "By the way, where did you get the mask?"

  j "Huh?"

  a "The mask in everyone's background."

  j "What are you talking about? Can we just play?"

  "A look of horror slowly dawns on Anaya's face."

  "Her computer screen ''GLITCHES''..."

  "{b}Good Ending{/b}."

  jump Credits

label Credits:
  "Thanks for playing Zoombomber!"

  "Written by: Jumai Yusuf"

  "Illustrations by: Toyin Yusuf"

  "Coding by and Zoom layout by: Tobi Yusuf"


return
