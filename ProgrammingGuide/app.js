var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var bodyParser = require('body-parser');
const session = require('express-session');

var index0Router = require('./routes/index');
var index1Router = require('./routes/index1');
var index2Router = require('./routes/index2');
var index3Router = require('./routes/index3');
var homeRouter = require('./routes/home');
var languagesRouter = require('./routes/languages');
var toolsRouter = require('./routes/tools');
var loginRouter = require('./routes/login');
var registerRouter = require('./routes/register');
var deleteRouter = require('./routes/delete');
var profileRouter = require('./routes/profile');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(session({
	secret: "myLittleSecretIsThatILoveYou<3",
	resave: false,
	saveUninitialized: true
}));

app.use('/0', index0Router);
app.use('/1', index1Router);
app.use('/2', index2Router);
app.use('/3', index3Router);
app.use('/home', homeRouter);
app.use('/languages', languagesRouter);
app.use('/tools', toolsRouter);
app.use('/login', loginRouter);
app.use('/register', registerRouter);
app.use('/delete', deleteRouter);
app.use('/profile', profileRouter);

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
