var path = require('path')
var webpack = require('webpack')

module.exports = {
  entry: './client/main.js',

  output: {
    path: path.resolve(__dirname, './server/static'),
    filename: 'build.js'
  },

  module: {
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          loaders: {
          }
          // other vue-loader options go here
        }
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      }
    ]
  }
}