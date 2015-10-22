 //////////////////////////////////////////////////Date Input Box Check!/////////////////////////////////
	$("#submit").click(function(){
   	$("#form1").validate({
	  rules:{
	  datetimepicker:"required",
	},
	messages:{
	  datetimepicker: "",
	}
	});  //表单验证
	if(!$("#form1").valid()){
	alert("请正确填写表单！");
	return false;
	}
	});
    //////////////////////////////////////////////////Date Input Box Check!/////////////////////////////////