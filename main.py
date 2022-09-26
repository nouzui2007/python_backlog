from backlog import Backlog

issueNumbers = [342, 340, 335, 334, 312, 346, 320, 318, 177, 295, 271, 274, 268, 277, 285]
assignee = '村中'
status = '修正済'
comment = 'ビルド30'

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
