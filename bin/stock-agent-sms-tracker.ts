#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { StockAgentSmsTrackerStack } from '../lib/stock-agent-sms-tracker-stack';

const app = new cdk.App();
new StockAgentSmsTrackerStack(app, 'StockAgentSmsTrackerStack', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: 'us-east-1'
  },

  // These will be populated from context or GitHub secrets
  twilioAccountSid: app.node.tryGetContext('twilioAccountSid'),
  twilioAuthToken: app.node.tryGetContext('twilioAuthToken'),
  toPhoneNumber: app.node.tryGetContext('toPhoneNumber'),
  fromPhoneNumber: app.node.tryGetContext('fromPhoneNumber'),
  finnhubApiKey: app.node.tryGetContext('finnhubApiKey'),
  openaiApiKey: app.node.tryGetContext('openaiApiKey'),

});

app.synth();

