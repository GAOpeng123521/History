# win开机后自动开启WSL并执行ssh/supervisor等服务

打开win10的启动文件夹（win+r后输入shell:startup）

新建ubuntuxx.vbs脚本文件

```
Set ws = CreateObject("Wscript.Shell")
ws.run "wsl -d Ubuntu -u root /etc/init.wsl start", vbhide
```

#上述代码第二行的Ubuntu根据自己安装的情况更改为其他相关版本，查看方法为win系统下命令行输入 wsl -l ，我的查看后就只有Ubuntu(默认) 对应代码只需填Ubuntu不用加后缀版本号



最后在WSL系统内新建编辑 /etc/init.wsl 文件

```
#!/bin/sh
/etc/init.d/ssh $1
/etc/init.d/supervisor $1
```

里面调用了我们希望启动的三个服务的启动脚本，设置权限为可执行，所有者为 root，这时候可以通过下面的脚本进行测试

```bash
sudo /etc/init.wsl [start|stop|restart]
```



参考https://zhuanlan.zhihu.com/p/47733615



# 挂载win下的外挂硬盘U盘

sudo mount -t drvfs E: /mnt/e





