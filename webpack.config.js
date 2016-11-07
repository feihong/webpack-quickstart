let path = require('path')
let BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  entry: './src/main.coffee',

  output: {
    path: './static/',
    filename: 'bundle.js'
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json', indent: 2}),
  ],

  module: {
    loaders: [
      {
        test: /\.coffee$/,
        loader: 'coffee-loader'
      },
      {
        test: /\.css$/,
        loader: 'style-loader!css-loader'
      },
      {
        test: /\.styl$/,
        loader: 'style-loader!css-loader!stylus-loader'
      }
    ]
  }
}
