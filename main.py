from backlog import Backlog

issueNumbers = [358, 391]
assignee = '村中'
status = '修正済'
comment = '再現しなくなっているので最新版でご確認ください。'

backlog = Backlog()

for n in issueNumbers:
    print(f'Update Issue#{n}')
    backlog.updateStatus(n, assignee, status, comment)

# 未対応
# 処理中
# 社内確認中
# 社外確認中
# 修正済
# IRGテスト待ち
# DADテスト待ち
# 処理済み
# 今後対応
# 保留
# 完了
