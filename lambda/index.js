exports.handler = (event, context, callback) => {
    var AWS = require('aws-sdk');
    var iotdata = new AWS.IotData({endpoint: 'a2zj3riqx6rtbe.iot.us-east-1.amazonaws.com'});

    var params = {
        topic: 'awsiot_to_localgateway',
        payload: 'PlayTheSong',
        qos: 0
    };

    iotdata.publish(params, function(err, data){
        if(err){
            console.log(err);
        } else{
            console.log('Published!');
        }
    });

    callback(null, 'Success!');
};