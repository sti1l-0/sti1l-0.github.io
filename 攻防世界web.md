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

## favorite_number

``` php	
<?php
//php5.5.9
$stuff = $_POST["stuff"];
$array = ['admin', 'user'];
if($stuff === $array && $stuff[0] != 'admin') { ##强等于，首项不等于
    $num= $_POST["num"];
    if (preg_match("/^\d+$/im",$num)){			##num中只有数字，多行匹配
        if (!preg_match("/sh|wget|nc|python|php|perl|\?|flag|}|cat|echo|\*|\^|\]|\\\\|'|\"|\|/i",$num)){##排除常用命令
            echo "my favorite num is:";
            system("echo ".$num);
        }else{
            echo 'Bonjour!';
        }
    }
} else {
    highlight_file(__FILE__);
}
```

- 绕过强等于用php5.5的数组溢出
- num的正则开启了多行匹配，可以通过添加%0a完成多行，再下一行添加命令
- 用$1、$@、反引号这些绕过命令的正则
- *利用ls -i读取文件的inode，不需要文件名就能指明文件*
- *创建变量ab分别等于f和lag利用$a$b拼接出flag*

## lottery

分析源码，看到api.php中用于判断中奖号码的函数是

``` php
for($i=0; $i<7; $i++){
		if($numbers[$i] == $win_numbers[$i]){	##这里用了弱等于
			$same_count++;
		}
	}
```

php在类型转换时，bool与非bool比较会把非bool转换为bool。构造请求传入字符串为true，使得比较时开奖号码转换即可。
