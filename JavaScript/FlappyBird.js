var cvs = document.querySelector("canvas");  
var ctx = cvs.getContext("2d");  
var bird = new Image();  
var bird2 = new Image();
var bg = new Image();  
var fg = new Image();  
var pipeNorth = new Image();  
var pipeSouth = new Image();  
var End = new Image();
var PlayAgain = new Image();
var Easy = new Image();
var Standard = new Image();
var Hard = new Image();
var Extreme = new Image();
var Skin1 = new Image();
var Skin2 = new Image();
var musik = new Audio();
var point = new Audio();
var dead = new Audio();
bird.src = "files/bird6.png"; 
bird2.src = "files/bird4.png";
Skin1.src = 'files/bird6.png';
Skin2.src = 'files/bird4.png';
PlayAgain.src = 'files/PlayAgain.png';
bg.src = "files/bg.png";  
fg.src = "files/fg.png";  
pipeNorth.src = "files/pipeNorth2.png";  
pipeSouth.src = "files/pipeSouth2.png";   
Easy.src = 'files/EASY.png';
Standard.src = 'files/STANDARD.png';
Hard.src = 'files/HARD.png';
Extreme.src = 'files/EXTREME.png';
musik.src = 'files/Musik.mp3'
point.src = 'files/point.mp3'
dead.src = 'files/hit.mp3'


var PlayAgainX = canvas.width-205;
var PlayAgainY = canvas.height/2;
var PlayAgainW = 140;
var PlayAgainH = 50;
var EasyX = 3;
var EasyY = canvas.height/2;
var EasyW = 66;
var EasyH = 40;
var StandardX = 72;
var StandardY = canvas.height/2;
var StandardW = 66;
var StandardH = 40;
var HardX = 144;
var HardY = canvas.height/2;
var HardW = 66;
var HardH = 40;
var ExtremeX = 216;
var ExtremeY = canvas.height/2;
var ExtremeW = 66;
var ExtremeH = 40;
var SkinX1 = 70;
var SkinY1 = 350;
var SkinH1 = 51;
var SkinW1 = 51;
var SkinX2 = 140;
var SkinY2 = 350;
var SkinH2 = 51;
var SkinW2 = 51;
var AllowMenu = true;
var easy;
var standard;
var hard;
var extreme;
var Change = true;
var death = true;
var gap; 
var distance;
var constant;  
var allowJump = true;
var allowSideways = false;
var bX = 10;  
var bY = 150;  
var Control = false;
var Start = false;
var gravity = 0.3;  
var gravitySpeed = 0;
var score = 0;  
var jump = 0;
var gameover = false;
var play = false;
var allowDeath = false;



function Easy(){
    gap = 150;
    distance = 50;
}
function Standard(){
    gap = 137;
    distance = 75;
}
function Hard(){
    gap = 110;
    distance = 100;
}
function Extreme(){
    gap = 100;
    distance = 120;
}
function fly(){
        var fly = new Audio();
        fly.src = "files/swoosh.mp3"
        fly.volume = 1
        fly.play()
}



function moveUp(){  
    bY -= 25;
    gravitySpeed = 0  
    return;
}   

document.addEventListener("keydown",(moveUp)=>{
    switch (moveUp.code){
        case 'ArrowUp':
            if(play){
            if (allowJump){
            bY -= 0 ;
            
            
            if(gravitySpeed>0){
                gravitySpeed=-1.3;
                
            };
            if(gravitySpeed<0){
                
                gravitySpeed = gravitySpeed -2.4;
                
            }; 
            if (gameover == false){
                jump = jump+1;
                fly();
            };

            
            allowJump = false;
            Start = true;
            
            
            
    };
};
            return 
            break;
            default:
                break;
    };
});  

document.addEventListener('keyup',(moveUp)=>{
    switch(moveUp.code){
        case 'ArrowUp':
            allowJump = true;
   }
})


  
var pipe = [];  
  
pipe[0] = {  
    x : cvs.width,  
    y : 0 
};  
function end(){
    location.reload();
}


function draw(){  
    
    ctx.drawImage(bg,0,0);  

    if(AllowMenu){
        ctx.font = 'Arial 30px';
        ctx.fillStyle = 'red';
        ctx.fillText('Choose AllowMenu!',+ cvs.width/4,100,150);
        ctx.fillText('Also choose skin if you wish',+cvs.width/4,120,150);
        ctx.fillStyle = 'cyan';
        ctx.fillRect(EasyX,EasyY,EasyW,EasyH);
        ctx.fillStyle = 'Yellow';
        ctx.fillRect(StandardX,StandardY,StandardW,StandardH);
        ctx.fillStyle = 'orange';
        ctx.fillRect(HardX,HardY,HardW,HardH);
        ctx.fillStyle = 'red';
        ctx.fillRect(ExtremeX,ExtremeY,ExtremeW,ExtremeH);
        ctx.drawImage(Easy,EasyX,EasyY);
        ctx.drawImage(Standard,StandardX,StandardY);
        ctx.drawImage(Hard,HardX,HardY);
        ctx.drawImage(Extreme,ExtremeX,ExtremeY);
        ctx.drawImage(Skin1,SkinX1,SkinY1);
        ctx.drawImage(Skin2,SkinX2,SkinY2);
        

        
        if(Change){
        canvas.addEventListener('click',function(event){
            if( AllowMenu &&
                event.x > EasyX &&
                event.x < EasyX + EasyW &&
                event.y > EasyY &&
                event.y < EasyY + EasyH
            ){
                gap = 137;
                distance = 70;
                AllowMenu = false;
                Control = true;
                play = true;
                Change = false;
                
            };
        });
    };
    if(Change){
        canvas.addEventListener('click',function(event){
            
            if( AllowMenu &&
                event.x > StandardX &&
                event.x < StandardX + StandardW &&
                event.y > StandardY &&
                event.y < StandardY + StandardH
            ){
                gap = 137;
                distance = 75;
                AllowMenu = false;
                Control = true;
                play = true;
                Change = false;
            };
        });
    };

    if(Change){
        canvas.addEventListener('click',function(event){
            if( AllowMenu &&
                event.x > HardX &&
                event.x < HardX + HardW &&
                event.y > HardY &&
                event.y < HardY + HardH
            ){
                gap = 110;
                distance = 100;
                AllowMenu = false;
                Control = true;
                play = true;
                Change = false;
            };
        });
    };
    if(Change){
        canvas.addEventListener('click',function(event){
            if( AllowMenu &&
                event.x > ExtremeX &&
                event.x < ExtremeX + ExtremeW &&
                event.y > ExtremeY &&
                event.y < ExtremeY + ExtremeH
            ){
                gap = 100;
                distance = 120;
                AllowMenu = false;
                Control = true;
                play = true;
                Change = false;
            };
        });

    };
    if(Change){
        canvas.addEventListener('click',function(event){
            if( AllowMenu &&
                event.x > SkinX1 &&
                event.x < SkinX1 + SkinW1 &&
                event.y > SkinY1 &&
                event.y < SkinY1 + SkinH1
            ){
                bird.src = 'files/bird6.png'
            }
        })
    }
    if(Change){
        canvas.addEventListener('click',function(event){
            if( AllowMenu &&
                event.x > SkinX2 &&
                event.x < SkinX2 + SkinW2 &&
                event.y > SkinY2 &&
                event.y < SkinY2 + SkinH2
            ){
                bird.src = 'files/bird4.png';
            };
        });
    };
};


    if(gameover){
        if (allowDeath){
            if(death){
                dead.play();
                death = false;
            };
        };
        cancelAnimationFrame(animationid);
        gravity = 0;
        gravitySpeed = 0;
        musik.muted = true;
        fg.removeAttribute('src');
        pipeNorth.removeAttribute('src');
        pipeSouth.removeAttribute('src');
        bird.removeAttribute('src');
        bg.removeAttribute('src');
        ctx.fillStyle = 'Black';
        ctx.fillRect(0,0,1000,1000);
        
        ctx.font = '100px Arial';
        ctx.fillStyle = 'red';
        ctx.fillText('You died!',cvs.width/2-70,cvs.height-400, 150);
              
        ctx.fillStyle = 'black';
        ctx.fillRect(PlayAgainX,PlayAgainY,PlayAgainW,PlayAgainH);
        canvas.addEventListener('click',function(event){
            if(
                event.x > PlayAgainX &&
                event.x < PlayAgainX + PlayAgainW &&
                event.y > PlayAgainY &&
                event.y < PlayAgainY + PlayAgainH
            ){
                end();
            };
        });
        ctx.drawImage(PlayAgain,canvas.width-205,canvas.height/2);
        
        
    };

      if(Start){
        gravitySpeed += gravity;
        bY += gravitySpeed;
        musik.play();
        musik.loop = true;

        Control = false;
        
        
    for(var i = 0; i < pipe.length; i++){  
          
        constant = pipeNorth.height+gap;  
        ctx.drawImage(pipeNorth,pipe[i].x,pipe[i].y);  
        ctx.drawImage(pipeSouth,pipe[i].x,pipe[i].y+constant);  
        
        pipe[i].x--;  
          
        if( pipe[i].x == distance ){  
            pipe.push({  
                x : cvs.width,  
                y : Math.floor(Math.random()*pipeNorth.height)-pipeNorth.height  
            });   
        };  
       
          
        if( bX + bird.width >= pipe[i].x && bX <= pipe[i].x + pipeNorth.width && (bY <= pipe[i].y + pipeNorth.height || bY+bird.height >= pipe[i].y+constant) || bY + bird.height >=  cvs.height - fg.height){
            
            
            
            allowDeath = true,
            allowJump = false;
            gameover = true;
            pipe[i].x =0;
            
        };  
        
        if(pipe[i].x == 1){  
            score = score+1; 
            point.play(); 
        };    
          
        
          
    };  
};
    ctx.drawImage(fg,0,cvs.height - fg.height);  
    ctx.drawImage(bird,bX,bY,50,50);
    

    if(Control){
        ctx.font = '25px Arial';
        ctx.fillStyle = 'red';
        ctx.fillText('Press Up to start!', + cvs.width/3,100,100)
    }; 
        

    
    
   
       
    
 
    ctx.fillStyle = "red";  
    ctx.font = "20px Verdana";  
    ctx.fillText("Score : "+score,10,cvs.height-20);  
    ctx.fillText('Jumps :' + jump,cvs.width-120,cvs.height-20);
    animationid = requestAnimationFrame(draw);  
};  



draw(); 
setInterval(() =>{
    console.log(bY)

    }, 100)