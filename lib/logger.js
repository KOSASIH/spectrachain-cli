class Logger {
  info(message) {
console.log(`[INFO] ${message}`);
  }

  error(message) {
    console.error(`[ERROR] ${message}`);
  }
}

export { Logger };
