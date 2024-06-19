import { NetworkManager } from './network';

class BlockchainManager {
  async getBlock(blockNumber) {
    const networkManager = new NetworkManager();

    try {
      const response = await networkManager.getBlock(blockNumber);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get block information: ${error}`);
    }
  }
}

export { BlockchainManager };
