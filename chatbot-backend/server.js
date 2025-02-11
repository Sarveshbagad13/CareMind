const express=require('express')
const morgan = require('morgan')
const server = express()
const cookieParser=require('cookie-parser')
const bcrypt=require('bcrypt')
const dbconnection = require('./config/db')
const userModel = require('./models/message')

server.use(morgan('dev'))
server.use(cookieParser())
server.use(express.json())
server.use(express.urlencoded({extended:true}))

server.use(express.static('public'));


server.set('view engine', 'ejs');
server.set('views', './views');

/*app.use((req,res,next) => {
    console.log('this is middleware')
     const a=3
     const b=6
     
     console.log(a*b)
S
     return next()

     return next()
})*/
server.get('/',(req,res) => {
    res.render('index')
})


server.get('/login', (req, res) => {
    res.render('login');  
});

server.get('/profile', (req, res) => {
  res.render('profile');  
});

/*server.post('/login', (req, res) => {
  const { email, password } = req.body;
 
  console.log('Login attempt:', { email, password });

  if (email === 'admin' && password === 'password') {
    res.send('Logged in successfully');
  } else {
    res.send('Invalid credentials');
  
});*/

server.get('/login', (req, res) => {
  res.render('login');
});

server.post('/get-form-data',(req,res) => {
    console.log(req.body)
    res.send("Data Received")
})


server.get('/register',(req,res) => {
    res.render('register')
}) 

/*app.post('/register',(req,res) => {
    console.log(req.body)
    res.send("user Registered")
})*/

server.get('/read',function (req,res) {
    console.log(req.cookies);
    res.send("read page");
})















server.listen(3000)
