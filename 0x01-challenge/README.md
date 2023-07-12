# 0x01. Fix my code
#### `Debugging`
### Background Context
`Fix my code` is a new type of project, where we’ll jump into an existing code base and fix it!

Sometime you will know the language, sometime not.

Please download the repository [0x01-Fix_My_Code_Challenge](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge) and use it as initial files for all solutions.

You should not recode everything, just fix it!

**This project is NOT mandatory** at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won’t get hurt if you don’t do it, but if your current average is greater than your score on this project, your average might go down. Have fun!

## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be compiled on Ubuntu `14.04` LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project is mandatory

## Tasks

[0. Server status](./status_server/)

I just started a new Flask project and the first thing I’m putting in place is a route for the status of my API (super important for a load balancer implementation).

But I don’t know why it’s not working…

Could you look at it and fix it please?

My code is [here](https://github.com/alx-tools/0x01-Fix_My_Code_Challenge/tree/master/status_server/)
```
$ python -m api.v1.app 
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
```
$ curl -XGET http://0.0.0.0:5000/api/v1/status
{
  "error": "Not found"
}
$
```
