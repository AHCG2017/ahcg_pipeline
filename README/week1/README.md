##Week1

##Change a remote’s URL in GitHub

1.Get the name of the remote you want to change.

```{sh}
git remote –v
```

2.Login in your GitHub account and click on one repository. Then copy the url. 

3.Change your remote's URL from SSH to HTTPS.

```{sh}
git remote set-url https://github.com/NAME/REPOSITORY
```

4.Verify that the remote URL has been changed

```{sh}
git remote –v
```

##Clone another repository 

```{sh}
git clone https://github.com/shashidhar22/ahcg_pipeline.git
```
##Ignore files
###Save the files you do not want to change in your github repository

1.
```
nano .gitignore
```

2.Add the folders you want to ignore before ```#local```

##Update on ahcg_pipeline.py
#####In ahcg_pipeline.py pipeline java call does not work

Replace 
```
java 
``` 
with 

```{sh}
/home/basespace/ahcg_pipeline/noupload/jre1.8.0_101/bin/java 
```


