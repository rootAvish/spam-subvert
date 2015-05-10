### Docu-fucking-mentation.

First get the enron database.
* http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron6.tar.gz
* http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron5.tar.gz
* http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron4.tar.gz
* http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron3.tar.gz
* http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron2.tar.gz
* ttp://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron1.tar.gz

This is the directory structure you want when you untar all of it:
![directory structure](/images/dirst.png)

Once this is done, You need to create two dummy mailboxes, one with only ham, and one with only spam. The way I did it was create a new user(hamuser) and forward all ham mail to him as with:

```bash
	 $python send-mail-ham.py hamuser@spam.com
```

Change the e-mail id as suitable. This script will run for a good 15 minutes or so, so be prepared to wait. Similarly for the spam mailbox, I create a 2nd user 'spamuser', and send him a mailbox full of spam with:

```bash
	$python send-mail-spam.py spamuser@spam.com
```

As we have to exclude our testing data from the training set, both the scripts will prompt you to enter an exclude list of directories, so for example, if you want to use enron5 and enron6 for testing, exclude them when prompted as with separating them with a space.


All this mail would be sent to the corresponding mailboxes and stored in the user's mbox in `/var/mail`.
Now train spambayes using the spools of mboxes you find under `/var/mail`

```bash
$sudo sb_filter.py -d /var/mail/hammie.db -n
Created new database in /var/mail/hammie.db

$sudo sb_mboxtrain.py -d /var/mail/hammie.db -s /var/mail/spamuser -g /var/mail/hamuser 
Training ham (/var/mail/hamuser):
  Reading as Unix mbox
  Trained 16545 out of 16545 messages
Training spam (/var/mail/spamuser):
  Reading as Unix mbox
  Trained 17171 out of 17171 messages
```

*Step X* -> Now run spambayes on a mbox to see the classifier in action, be sure to pass in your hammie.db.

```bash
$sb_filter.py -d/var/mail/hammie.db mailuser1 > ~/primary.txt
```

I sent testing data to mailuser1, change this accordingly. Don't touch the hamuser and spamuser mailboxes, they are pure ones we used for training. I redirected the output to result.txt

Then run get_result.py on the file you just wrote to, to get spam scores of all mails in that mailbox.

```bash
$python get_result.py primary.txt before.txt && cat before.txt
X-Spambayes-Classification: unsure; 0.50
X-Spambayes-Classification: spam; 0.98
X-Spambayes-Classification: unsure; 0.74
X-Spambayes-Classification: unsure; 0.27
X-Spambayes-Classification: unsure; 0.27
X-Spambayes-Classification: unsure; 0.27
X-Spambayes-Classification: unsure; 0.27
X-Spambayes-Classification: unsure; 0.27
X-Spambayes-Classification: spam; 0.94
```

The second file is obvio, the one where you want your result.

Now, this is where you come in. Remember the mail we just sent to mailuser1, and compiled the result? Well, now delete `/var/mail/mailuser1`, then create a blank mailbox, as with ```bash $cd /var/mail && sudo touch mailuser1```

Now, send the 'optimized e-mails.' Once that's done, and you have a new mailbox, repeat from step X.

Then we can figure out a way to compare both results, like say draw a graph. I'll take care of that but that's for a later time.

Please feel free to contact me for any further queries :wink:.

###Okay, here is what Antriksh did:

First, here is how the parser script works for now:
	python parser.py <filename>
	
What this script is doing is checking if in in common nouns a word is existing and replaces that word with the noun if there is one and if there is not, removes the word.

Only checked for noun uptill now.
