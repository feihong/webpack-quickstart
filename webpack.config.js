let path = require('path')
let BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  entry: {
    main: './src/main.coffee',
    cool: './src/cool.coffee',
  },

  output: {
    path: './static/',
    filename: '[name].js'
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
