class StorageManager {
  saveAuthToken(authToken) {
    localStorage.setItem('spectrachainAuthToken', authToken);
  }

  getAuthToken() {
    return localStorage.getItem('spectrachainAuthToken');
  }
}

export { StorageManager };
