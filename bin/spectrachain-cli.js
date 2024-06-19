#!/usr/bin/env node

import { Command } from 'commander';
import { AccountManager } from '../lib/account';
import { BlockchainManager } from '../lib/blockchain';
import { CryptoManager } from '../lib/crypto';
import { Logger } from '../lib/logger';
import { NetworkManager } from '../lib/network';
import { StorageManager } from '../lib/storage';

const program = new Command();

program
 .version('1.0.0')
 .description('SpectraChain CLI');

program
 .command('login')
 .description('Login to SpectraChain')
 .action(async () => {
    const logger = new Logger();
    const networkManager = new NetworkManager();
    const storageManager = new StorageManager();

    try {
      await networkManager.login();
      storageManager.saveAuthToken(networkManager.getAuthToken());
      logger.info('Logged in successfully!');
    } catch (error) {
      logger.error('Login failed:', error);
    }
  });

program
 .command('me')
 .description('Get user information')
 .action(async () => {
    const logger = new Logger();
    const storageManager = new StorageManager();
    const accountManager = new AccountManager();

    try {
      const authToken = storageManager.getAuthToken();
      const userInfo = await accountManager.getUserInfo(authToken);
      logger.info(`User Information: ${JSON.stringify(userInfo, null, 2)}`);
    } catch (error) {
      logger.error('Failed to get user information:', error);
    }
  });

program
 .command('send <amount> <recipientAddress>')
 .description('Send cryptocurrency')
 .action(async (amount, recipientAddress) => {
    const logger = new Logger();
    const storageManager = new StorageManager();
    const cryptoManager = new CryptoManager();

    try {
      const authToken = storageManager.getAuthToken();
      await cryptoManager.sendCryptocurrency(authToken, amount, recipientAddress);
      logger.info(`Sent ${amount} cryptocurrency to ${recipientAddress} successfully!`);
    } catch (error) {
      logger.error('Failed to send cryptocurrency:', error);
    }
  });

program
 .command('blockchain:get-block <blockNumber>')
 .description('Get block information')
 .action(async (blockNumber) => {
    const logger = new Logger();
    const blockchainManager = new BlockchainManager();

    try {
      const blockInfo = await blockchainManager.getBlock(blockNumber);
      logger.info(`Block Information: ${JSON.stringify(blockInfo, null, 2)}`);
    } catch (error) {
      logger.error('Failed to get block information:', error);
    }
  });

program.parse(process.argv);
