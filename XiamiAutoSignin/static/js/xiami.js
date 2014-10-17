function validate_required(field,alerttxt)
{
	with (field)
	  {
		  if (value==null||value=="")
		    {alert(alerttxt);return false}
		  else {return true}
	  }
}
function validate_email(field,alerttxt)
{
	with (field)
	{
		apos=value.indexOf("@")
		dotpos=value.lastIndexOf(".")
		if (apos<1||dotpos-apos<2) 
		  {alert(alerttxt);return false}
		else {return true}
	}
}
function validate_form(thisform)
{
	with (thisform)
	  {
		if (validate_email(email,"请输入正确的email地址!")==false)
				{email.focus();return false}
	  	if (validate_required(password,"你的肥皂忘记扔了!")==false)
	    	{password.focus();return false}
	  }
}