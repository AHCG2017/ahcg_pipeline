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

