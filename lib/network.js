import axios from 'axios';

class NetworkManager {
  async login() {
    try {
      const response = await axios.post('https://spectrachain.io/api/login', {
        username: 'your_username',
        password: 'your_password',
      });
      return response.data.authToken;
    } catch (error) {
      throw new Error(`Login failed: ${error}`);
    }
  }

  async getUserInfo(authToken) {
    try {
      const response = await axios.get('https://spectrachain.io/api/user-info', {
        headers: {
          Authorization: `Bearer ${authToken}`,
        },
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get user information: ${error}`);
    }
  }

  async sendCryptocurrency(authToken, amount, recipientAddress) {
    try {
      const response = await axios.post('https://spectrachain.io/api/send-cryptocurrency', {
        amount,
        recipientAddress,
      }, {
        headers: {
          Authorization: `Bearer ${authToken}`,
        },
      });
      return response.data;
    } catch (error) {
      throw new Error(`Failed to send cryptocurrency: ${error}`);
    }
  }

  async getBlock(blockNumber) {
    try {
      const response = await axios.get(`https://spectrachain.io/api/block/${blockNumber}`);
      return response.data;
    } catch (error) {
      throw new Error(`Failed to get block information: ${error}`);
    }
  }
}

export { NetworkManager };
