const path = require('path')

module.exports = {
    output: {
        path: path.join(__dirname, '/dist'),
        filename: 'index.bundle.js'
    },
    devServer: {
        port: 80,
        hot: true,
        allowedHosts: [
            'saiarts.dev'
        ]
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            },
             {
                test: /\.scss$/,
                use: [
                    'style-loader',
                    'css-loader',
                    'sass-loader'
                ],
            },
            {
                test: /\.(eot|ttf|JPG|svg|woff|woff2|png|jpe?g|gif)$/,
                use: [
                  {
                    loader: 'file-loader',
                  },
                ],
              },
            
        ]
    },
    resolve: {
        alias: {
            '@mui/styled-engine': '@mui/styled-engine-sc'
            },
        },
}