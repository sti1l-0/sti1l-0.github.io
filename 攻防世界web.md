## web2

```php	
    for($_0=0;$_0<strlen($_o);$_0++){
       
        $_c=substr($_o,$_0,1);		//选取一位字符
        $__=ord($_c)+1;				//ascii加1
        $_c=chr($__);				//再转回字符
        $_=$_.$_c;   				//拼回去
    } 
    return str_rot13(strrev(base64_encode($_)));
```

## 