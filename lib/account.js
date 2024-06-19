import { NetworkManager } from './network';
import { StorageManager } from './storage';

class AccountManager {
  async getUserInfo(authToken) {
    const networkManager = new NetworkManager();
    const storageManager = new StorageManager();

    try {
      const response = await networkManager.getUserInfo(authToken);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get user information: ${error}`);
    }
  }
}

export { AccountManager };
