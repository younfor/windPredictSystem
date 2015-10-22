 ///////////////////      mousewheel pic bigger or smaller   /////////////////////////

function zoomImg(o) {
var zoom = parseInt(o.style.zoom, 10) || 100;
zoom += event.wheelDelta / 10; //可适合修改
if (zoom > 0)
o.style.zoom = zoom + '%';
}
$(document).ready(function() {
$("img").bind("mousewheel", function() {
zoomImg(this);
return false;
});
});



function bigOrSmaller(){
   $("img").bind("mousewheel", function() {
zoomImg(this);
return false;
});

}
///////////////////      mousewheel pic bigger or smaller   /////////////////////////


var imgFirst = "<img src= " + "'" ;
var imgLast =   "' "+ "/>";

/////////////////////////      div1Click      /////////////////////////////
function div1Click(){
     $("#div1").validate({
    rules:{
   Dm: {
        required:true,
        number:true
    },
   Ht: {
        required:true,
        number:true
    },
   datetimepicker1: "required",
  },
messages:{
  Dm: {
      required:"",   
     },
   Ht: {
      required:"",   
     },
  datetimepicker1: "",
}
});  //表单验证
if(!$("#div1").valid()){
alert("请正确填写表单！");
return false;
}
     var Dm = $("#Dm").val();
     var Ht= $("#Ht").val();
     var Dt= $("#datetimepicker1").val();


     var params = {'Dm':Dm,'Ht':Ht,'Dt':Dt};
       $.ajax({
         async:true,
          type:'get',
          url:'/wind/weatherDiv1',
          data:params,
          cache:false,
          dataType:'json',
          beforeSend:function(XMLHttpRequest){ 
              MaskUtil.mask("Dealing,please wait 。。。");  
         }, 
        success:function (data) {
        MaskUtil.unmask();  
        var pic1 = document.getElementById("picDiv1");
        pic1.innerHTML="";
        var img = imgFirst + data + imgLast
 //       alert(img);
        pic1.innerHTML = img;
        bigOrSmaller();
          },
          error: function (json) {
              alert("json=" + json);
          }
      });
  }


/////////////////////////      div2Click      /////////////////////////////
function div2Click(){
     $("#div2").validate({
    rules:{
   Dm2: {
        required:true,
        number:true
    },
   Lat: {
        required:true,
        number:true
    },
   Lon:{
        required:true,
        number:true
    },
   Agh: {
        required:true,
        number:true
    },
   datetimepicker2: "required",
   datetimepicker3: "required",
  },
messages:{
  Dm2: {
      required:"",   
     },
   Lat: {
      required:"",   
     },
   Lon:{
      required:"",   
     },
   Agh: {
      required:"",   
     },
   datetimepicker2: "",
   datetimepicker3: "",
}
});  //表单验证
if(!$("#div2").valid()){
alert("请正确填写表单！");
return false;
}
     var Dm = $("#Dm2").val();
     var Lat= $("#Lat").val();
     var Lon= $("#Lon").val();
     var Agh = $("#Agh").val();
     var St= $("#datetimepicker2").val();
     var Et= $("#datetimepicker3").val();
     var imgFirst = "<img src= " + "'" 
     var imgLast =   "'"+ "/>";
     var params = {'Dm':Dm,'Lat':Lat,'Lon':Lon,'Agh':Agh,'St':St,'Et':Et};
       $.ajax({
         async:true,
          type:'get',
          url:'/wind/weatherDiv2',
          data:params,
          cache:false,
          dataType:'json',
          beforeSend:function(XMLHttpRequest){ 
              MaskUtil.mask("Dealing,please wait 。。。");  
         }, 
        success:function (data) {
        MaskUtil.unmask();  
        var dd = eval("([" + data + "])");
        $('#picDiv2').css('border','1px solid #ccc');
        echartDiv("picDiv2",dd[0],dd[1]);
          },
          error: function (json) {
              alert("json=" + json);
          }
      });
  }

/////////////////////////      div3Click      /////////////////////////////

 var $mask,$maskMsg;  
function div3Click(){
$("#div3").validate({
  rules:{
  Dm3: {
        required:true,
        number:true
    },
},
messages:{
  Dm3: {
      required:"",   
     },
}
});  //表单验证
if(!$("#div3").valid()){
alert("请正确填写表单！");
return false;
}
     var Dm = $("#Dm3").val();
 //    alert(Dm);
  var params = {'Dm':Dm};
       $.ajax({
         async:true,
          type:'get',
          url:'/wind/weatherDiv3',
          data:params,
          cache:false,
          dataType:'json',
          
        success:function (data) {
        MaskUtil.unmask();
        var pic3 = document.getElementById("picDiv3");  
        pic3.innerHTML="";
        var img = imgFirst + data+ imgLast
        console.log(img);
        pic3.innerHTML += img;
       bigOrSmaller();
          },
          beforeSend:function(XMLHttpRequest){ 
              MaskUtil.mask("Dealing,please wait 。。。");  
         }, 
          error: function (json) {
              alert("json=" + json);
          }
      });
  }

/////////////////////////////////用户等待提醒/////////////////////////////////

var MaskUtil = (function(){  
      
    var $mask,$maskMsg;  
      
    var defMsg = 'Dealing,please wait 。。。';  
      
    function init(){  
        if(!$mask){  
            $mask = $("<div></div>")  
            .css({  
              'position' : 'absolute'  
              ,'left' : '0'  
              ,'top' : '0'  
              ,'width' : '100%'  
              ,'height' : '100%'  
              ,'opacity' : '0.3'  
              ,'filter' : 'alpha(opacity=30)'  
              ,'display' : 'none'  
              ,'background-color': '#ccc'  
              ,'z-index':'1'
            })  
            .appendTo("body");  
        }  
        if(!$maskMsg){  
            $maskMsg = $("<div></div>")  
                .css({  
                  'position': 'absolute'  
                  ,'top': '50%'  
                  ,'margin-top': '-20px'  
                  ,'padding': '5px 20px 5px 20px'  
                  ,'width': 'auto'  
                  ,'border-width': '1px'  
                  ,'border-style': 'solid'  
                  ,'display': 'none'  
                  ,'background-color': '#ffffff'  
                  ,'font-size':'14px'  
                })  
                .appendTo("body");  
        }  
          
        $mask.css({width:"100%",height:$(document).height()});  
          
        var scrollTop = $(document.body).scrollTop();  
          
        $maskMsg.css({  
            left:( $(document.body).outerWidth(true) - 190 ) / 2  
            ,top:( ($(window).height() - 45) / 2 ) + scrollTop  
        });   
                  
    }  
      
    return {  
        mask:function(msg){  
            init();  
            $mask.show();  
            $maskMsg.html(msg||defMsg).show();  
        }  
        ,unmask:function(){  
            $mask.hide();  
            $maskMsg.hide();  
        }  
    }  
      
}());  

 function doSomething(msg){  
    MaskUtil.mask(msg);  
     setTimeout(function(){  
        // 模拟操作时间,3秒后关闭  
        MaskUtil.unmask();  
  
    },3000);  
} 

 /////////////////////////////////用户等待提醒/////////////////////////////////







  ////////////////////////////////////////speedchange//////////////////////////////////////////////////

   var t;
   var speed = 6;//图片切换速度
   var nowlan=0;//图片开始时间
   var mul=50;

     $(function() {
     $( "#slider").slider({
           orientation: "horizontal",
         range:"min",
           value: 50,
      // slide: changespeed,
          change: changespeed
       });
        $( "#slider" ).slider( "value", 50 );
   });

  function changespeed(){
   mul=100-$( "#slider" ).slider( "value" )*0.8;
  }

  function changepic() {
  var imglen = $("div[name='pic']").find("div").length;
  $("div[name='pic']").find("div").hide();
  $("div[name='pic']").find("div").eq(nowlan).show();
  nowlan = nowlan+1 ==imglen ?0:nowlan + 1;
  t = setTimeout("changepic()", speed*mul);
  }
$(document).ready(function () {
//鼠标在图片上悬停让切换暂停
$("div[name='pic']").hover(function () { clearInterval(t); });
//鼠标离开图片切换继续
$("div[name='pic']").mouseleave(function () { changepic(); });
changepic();
});

 ////////////////////////////////////////speedchange//////////////////////////////////////////////////

////////////////////////////////////////////////echart///////////////////////////////////////////////////
       // Step:3 echarts & zrender as a Global Interface by the echarts-plain.js.
        // Step:3 echarts和zrender被echarts-plain.js写入为全局接口
function echartDiv(divName,xdata,ydata){
  var myChart = echarts.init(document.getElementById(divName));
  option={

    title:{
      text:'风速'
    },
    tooltip : {
                    trigger: 'axis'
                },
    legend:{
      //orient:'horizontal',
      //backgroundColor:'#eee',
      data:['speed']
      },

  calculable : true,
  toolbox: {
                show : true,
                feature : {
                  /*  mark : {show: true},*/
                    dataZoom:{show:true},
                 /*   dataView : {show: true, readOnly: false},*/
                    magicType : {show: true, type: ['line', 'bar']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },

           dataZoom : {
           show : true,
           realtime: true,
           start : 0,
           end : 100
       },
    xAxis:[
      {
      type:'category',
      /*boundaryGap : false,*/
      data:xdata

    
      }
    ],

    yAxis:[     
      {
      type:'value',
      axisLabel:{
        formatter:'{value} mJ'},
      },      
    ],
    
    series:[
      {
      name:'speed',
      type:'line',
      symbol:'none',
      itemStyle: {
                    normal: {
                          color: 'red',
                             lineStyle: {        // 系列级个性化折线样式
                                 width: 1,
                                 type: 'solid'
                              }
                        },
                   },
      data:ydata,
      /*markPoint : {
                     data : [
                          {type : 'max', name: '最大值'},
                          {type : 'min', name: '最小值'}
                       ]
                   },*/
      /* markLine : {
                      data : [
                         {type : 'average', name: '平均值'}
                       ]
                 }*/
     
      },
    ],
};
    myChart.setOption(option);
}
////////////////////////////////////////////////echart///////////////////////////////////////////////////
