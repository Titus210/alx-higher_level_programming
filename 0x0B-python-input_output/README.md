## 		FILE HANDLING 
***
###	Inroduction
**FIle management**: THis is manipulation of data in a file.<br/>
**File**: This is a resurce of recording data discretedly in computercomputer device.
### 		File operations
**File handling**<br/>
We can perform various operations on files that includes: <br/>
-	Opening a file.
-	Read or write perform action.
-	closing a file.

1.	openning a file:
we use `open ()` method to open a file 
It takes 3 arguments: 
-		filename
-		mode: this is a mode we wanrt to open the file
-		character encoding.

```
	# opening in current directoruy
	f = open("new.txt", mode = "r", encoding = "uft-8")

	# fullpath directory
	f = open("/home/new/python/new.txt", mode = "r", encoding = "uft-8")```
**Types of mode**
`'r'` - Read: This mode is the default for open() method it opens file for reading
`'a'` - append: This mode opens for appending tht is it creates files if it does not exist and appends data inside else if it exists it creates adds data without truncationf
`'w'` - write: This mode writeds data in a file and if file exists it cruncates and rewrites everything inside.
`'x'` -  This mode opens file in exclusive creation and fails if file already exists
`'t'` - text: This is default mode for files to open in text mode.
`'b'` - binary: This is used to write data in binary form i.e image.

