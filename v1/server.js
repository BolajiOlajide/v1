const StaticServer = require('static-server');

const server = new StaticServer({
  rootPath: './output',            // required, the root of the server file tree
  port: process.env.PORT || 3000,  // required, the port to listen
  name: 'my-static-server',        // optional, will set "X-Powered-by" HTTP header
  // host: '10.0.0.100',           // optional, defaults to any interface
  cors: '*',                       // optional, defaults to undefined
  templates: {
    index: 'index.html',           // optional, defaults to 'index.html'
    notFound: '404.html'           // optional, defaults to undefined
  }
});

server.start(function () {
  console.log('Server listening to', server.port);
});
