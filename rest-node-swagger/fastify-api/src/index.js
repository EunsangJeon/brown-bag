// Hello world!
const fastify = require('fastify')({
  logger: true
});

// Hello world!
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/mycargarage').then(
  () => console.log('MongoDB connected…')
).catch(err => console.log(err));

// Swagger
const swagger = require('./config/swagger');
fastify.register(require('fastify-swagger'), swagger.options);

// Routes
const routes = require('./routes');
routes.forEach((route, index) => {
  fastify.route(route)
})

// Hello world!
fastify.get('/', (request, reply) => {
  reply.send({ hello: 'world' })
});

// Hello world!, Swagger
const start = async () => {
  try {
     await fastify.listen(3000, '0.0.0.0');
     fastify.swagger();
     fastify.log.info(`server listening on ${fastify.server.address().port}`);
  } catch (err) {
     fastify.log.error(err);
     process.exit(1);
  }
};
start();
