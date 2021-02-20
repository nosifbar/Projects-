#include <iostream>

using namespace std;

int main()
{
    cout<<"Type in your name!\n";
    string username;
    cin>>username;              //Asks for user name
    cin.ignore();
    cout<<"Welcome "<<username<<" to the WEIRDEST ADVENTURE GAME YOU WILL EVER SEE";
    cin.get();
    int plane;
    cout<<"You are stranded in the desert and have no idea where you are you see a plane"<<endl<<"and a pistol what do you choose";
    cout<<" 1 is plane"<<" 2 is pistol";
    cin>>plane;             //Asks to choose between plane or pistol
    
switch (plane)
{
    case 1:                     //If user selects plane:
            cout<<"you hop into the plane and it turns out to be infested with zombies"<<endl<<"you have died";
            cin.get();
            cout<<" ";
            cin.get();
        break;
        
    case 2:         //If user selects pistol
            cout<<"so you decide to grab the pistol ";
            cout<<"while you grab the pistol you notice something.. in the plane ";
            cout<<"it is a bunch of zombies you shoot them and they pass out for 5 minutes but you hop into the plane and leave ";
            cout<<"while the zombies are passed out.";
                cin.get();
            cout<<"you realise the plane is out of fuel so you land and get out";
            cout<<"the first thing you see is a deserted motel ";
            cout<<"you decide to stay awile.";
            cin.get();
            cout<<"in the distance you see something comin towards you...IT'S A GIANT CRAB!";
            cin.get();
            cout<<"It randomly falls into the sand a pops out cooked right into the Motel's pool";
            cin.get();
        int dinosaur;
            cout<<"you see something else coming...but this time its not a crabs ITS A DINOSAUR"<<endl;
            cout<<"do you hold still or hide in the motel ";
            cout<<"pick 1 to hold still"<<endl<<" pick 2 to hide in the motel"; //Asks to choose between hold or hide
        cin>>dinosaur;
        cin.get();
        
switch (dinosaur){
    case 1:                     //If user selects to hold still
        cout<<"the dinosaur stares at your for 15 minutes then lets you climb onto it and takes you to the forest";
        cin.get();
        cout<<"In the forest you meat a guy named "<<username<<" which is turns out to be you.";
        cin.get();
        cout<<"FROM THE FUTURE! and he leads you home";
        cin.get();
        cout<<"then in 5 years you go back in time lead your oldself home";
        cin.get();
        cout<<"you have survived";
        cout<<" ";
        cin.get();
        break;
        
    case 2:                         //If user selectd to hide in the motel
        cout<<"You hide in the motel.";
        cin.get();
        cout<<"how do you plan on getting out of this place?"<<endl<<"o well lets get back to the story.";
        cout<<"so the Dinosaur saw you go into the motel so it starts bashing the wall"<<endl<<"you see an Assualt rifle in another room";
        int rifle;
        cout<<" should you grab the rifle and shoot at the dinosaur or hide in the other room"<<endl<<"1 grab the rifle and shoot it"<<endl<<"2 hide";      //Asks to grab a rifle or to hide
        cin>>rifle;
        cin.get();
        
        
switch (rifle){
    case 1:                        //If user selects to grab a rifle and shoot
        cout<<"So you grab the rifle at shoot at it with your M4."<<endl<<"its ineffective and the dinosaur chases you then you trip."<<endl;
        cin.get();
        cout<<"you almost get eaten by it but it trips over a pebble and squishes you like a fly.";
        cin.get();
        cout<<" ";
    break;
        
    case 2:                         //If user selects to hide
        cout<<"You Dash into the room!";
        cout<<"the dinosaur oddly walks away."<<endl<<"you can't figure out why...";
        cout<<"THEN YOU TURN AROUND AND SEE YOUR NOT IN A MOTEL ITS A ALIEN AIRCRAFT CARRIER INSTEAD"<<endl;
        cin.get();
        cout<<"theres an aircraft in front of you";
        cout<<"1 hop into it"<<endl<<"2 wait"<<"3 Run away";  //Asks user to hop, wait or run away
        int alien;
        cin>>alien;
        cin.get();
        
switch (alien){
    case 1:                 //If user selects to hop
        cout<<"you fly the alien ship away"<<endl<<"Auto pilot is on and your going up to space"<<endl;
        cin.get();
        cout<<"turns out 3 species are fighting. Humans, Primarians, and the Renols"<<endl;
        cout<<"your in a Primarian ship. You begin to learn some controls then you see it"<<endl;
        cin.get();
        cout<<"A giant ship with a nuke headed towards it."<<endl;
        cout<<"It blows up and all out war starts!"<<endl;
        cin.get();
        cout<<"your now in dogfighting with some Renols. Yout take down like 3 of them";
        cout<<"then another nuke comes in and blows everything up";
        cin.get();
        
    case 2:                 //If user selects to wait
        cout<<"You wait and get abducted by Human Scientist that make you help them find the launch code for several alien nukes"<<endl;
        cin.get();
        cout<<"then you get put in jail for helping terrorist"<<endl<<"at least you survived right?";
        cin.get();
        
    case 3:             //If user selects to run away
        cout<<"the dinosaur sees you coming and runs you over";
        cin.get();
}
}
}
}
}

