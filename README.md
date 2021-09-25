# Baked Goods

Baked Goods is a simple python script to let you get your cookies into the
standard Netscape Cookie format.

**NOTE:** Firefox users will have to copy cookie fields one-by-one and
insert tabs between each field.

Chromium-based browsers will allow you to simply drag-select all the fields.
This is why if you want to use this script it is recommended that you use a
Chromium browser to get those cookies. A good browser to use for that purpose
is the Brave browser, but any other Chromium-based browser will do.

## How To Get Your Cookies

In order to get your cookies just:

1. Go to whatever site you want to get the cookies from

2. Open up the developer tools

3. Go to the ***Storage*** section, it should be at the top, if it's not there,
   then click on the right arrow near the top to reveal it

4. Look to the left and you will see a section called ***Cookies***, go there.

5. You will see a list of cookies broken down by website domain name, click on
   the one you want the cookies for

6. Click and drag over the cookies that are now off to the right. Make sure to
   select each row containing the cookie you want in its entirety or at least
   up until the **HttpOnly** column. You don't need to be precise with this,
   you can just select them all, the script should be able to handle that.

7. Paste what you just copied into a text file somewhere and save it, make sure
   to remove any blank lines. The blank lines won't break the script but you
   might as well not have them there in the first place

8. Run the script on that file

9. Profit

## Usage

``` baked_goods.py FILE...  ```

Where `FILE` is a file containing your cookies, you can specify multiple of
them.

Once you run the script the cookies will be parsed and then printed to standard
output if everything goes well. You can then use these in whatever application
you would like to use them in

If things do not go well a failure message will be printed to standard error
showing which line caused the issue. This happens mostly because there there
was a blank line in the file or the cookies being copied incorrectly
