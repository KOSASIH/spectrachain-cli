import { NetworkManager } from './network';
import { StorageManager } from './storage';

class CryptoManager {
  async sendCryptocurrency(authToken, amount, recipientAddress) {
    const networkManager = new NetworkManager();
    const storageManager = new StorageManager();

    try {
      const response = await networkManager.sendCryptocurrency(authToken, amount, recipientAddress);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to send cryptocurrency: ${error}`);
    }
  }
}

export { CryptoManager };
