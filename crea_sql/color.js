var Link={
SetColor:function (color){
 // var alist=document.querySelectorAll('a');
 // var i=0;
 // while(i<alist.length){
 // alist[i].style.color=color;
 //   i=i+1;
 // }
 $('a').css('color',color);
 }
}

var Body={
setBackGroundColor:function(color){
$('body').css('backgroundColor',color)  ;
},
setColor:function(color){
$('body').css('color',color)  ;
}
}

function NightDayHandler(self){
 var target=document.querySelector('body')
   if(self.value==='night'){
     Body.setColor('white');
     Body.setBackGroundColor('black')
     Link.SetColor('powderblue');
     self.value='day';
   }
   else{
     Body.setColor('black');
     Body.setBackGroundColor('white');
     Link.SetColor('white');
     self.value='night';
    }
}
